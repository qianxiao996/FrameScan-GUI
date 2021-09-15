# coding:utf-8
import json
import re
import traceback

import ProbeDefine


# from app import app


class PostSuffix(object):
	def __init__(self, oLogger=None):
		self.LEVEL = {
			"&&": 1,
			"||": 0,
			"(": 999,
			")": 999
		}
		self.oLogger = oLogger

	def set_level(self, level):
		self.LEVEL = level

	def is_operator(self, c):
		if c.strip() in self.LEVEL.keys():
			return True

	def _get_level(self, operator_str):
		return self.LEVEL.get(operator_str, 0)

	def _compare(self, option, option1):
		option_leve = self._get_level(option)
		option1_leve1 = self._get_level(option1)
		return option_leve >= option1_leve1

	def _split_expression_str(self, expression_str):
		regex = "(\|\|)|(&&)|(\()|(\))"
		expression_list = [x for x in re.split(regex, expression_str) if x and x.strip()]
		return expression_list

	def _suffix(self, expression_list):
		results = []
		stack = []
		for item in expression_list:
			if self.is_operator(item):
				if item == ")":
					if len(stack) == 0:
						continue
					top = stack.pop()
					while top != "(":
						results.append(top)
						top = stack.pop()
				else:
					if len(stack) == 0:
						stack.append(item)
						continue

					top = stack[-1]
					while self._compare(top, item) and top != "(":
						results.append(stack.pop())
						if len(stack) == 0:
							break
						top = stack[-1]
					stack.append(item)
			else:
				results.append(item)
		if len(stack) > 0:
			results.extend(stack[::-1])
		return results

	def suffix(self, expression_str, return_type="suffix", is_poc_match=False):
		ret = []
		mapSeedRules = {}
		try:
			if self.is_double_quote_suffix_match() or is_poc_match:
				expression_str, mapSeedRules = self.double_quote_format_match(szRuleExp=expression_str)
			elif self.is_bracket_suffix_match():
				expression_str = self.bracket_foramt_match(search_str=expression_str)
			expression_list = self._split_expression_str(expression_str)
			ret = self._suffix(expression_list)

			if self.is_bracket_suffix_match():
				ret = self.replace_bracket(ret)

			if return_type == 'list':
				ret = self._handle_ret2_list(ret)
			else:
				pass
		except Exception as e:
			ret = []
			mapSeedRules = {}
			if self.oLogger:
				self.oLogger.error(traceback.format_exc(e))
				self.oLogger.error('PostSuffix: Convert expression string to suffix failed, expression=[%s], type=[%s]' % (expression_str, return_type))
		return ret, mapSeedRules

	def _handle_ret2_list(self, suffix):
		temp_result = []
		for item in suffix:
			ret_list = []
			if self.is_operator(item):
				len_temp_result = len(temp_result)
				if len_temp_result >= 2:
					ret_list.append(temp_result.pop())
					ret_list.append(temp_result.pop())
					ret_list.append(item)
					temp_result.append(ret_list)
			else:
				temp_result.append(item)
		if len(temp_result) == 0:
			return []
		if isinstance(temp_result[0], list):
			return temp_result[0]
		else:
			return temp_result

	def adjust_rule_symbols(self, szRuleExp):
		if szRuleExp.startswith('&&'):
			szRuleExp = szRuleExp.replace('&&', '', 1)
		if szRuleExp.startswith('||'):
			szRuleExp = szRuleExp.replace('||', '', 1)
		szRuleExp = szRuleExp[::-1]
		if szRuleExp.startswith('&&'):
			szRuleExp = szRuleExp.replace('&&', '', 1)
		if szRuleExp.startswith('||'):
			szRuleExp = szRuleExp.replace('||', '', 1)
		szRuleExp = szRuleExp[::-1]
		szRuleExp = szRuleExp.replace("（", "(").replace("）", ")")
		return szRuleExp

	def bracket_foramt_match(self, search_str):
		search_str = self.adjust_rule_symbols(szRuleExp=search_str)
		search_strs = [x for x in re.split("(\()|(\))", search_str) if x and x.strip()]
		temp = []
		for i in range(len(search_strs)):
			if search_strs[i] == '(':
				temp.append((i, search_strs[i]))
			if search_strs[i] == ')':
				if len(temp) > 0:
					j, left_bracket = temp.pop()
					if j == 0 and i == len(search_strs) - 1:
						search_strs[j] = search_strs[j].replace(search_strs[j], '')
						search_strs[i] = search_strs[i].replace(search_strs[i], '')
					elif j == 0 and i < len(search_strs) - 1:
						if search_strs[i + 1].strip()[:2] != "||" and search_strs[i + 1].strip()[:2] != "&&":
							search_strs[j] = search_strs[j].replace(search_strs[j], '$$$$000')
							search_strs[i] = search_strs[i].replace(search_strs[i], '$$$$111')
					elif j > 0 and i == len(search_strs) - 1:
						if search_strs[j - 1].strip()[-2:] != "||" and search_strs[j - 1].strip()[-2:] != "&&":
							search_strs[j] = search_strs[j].replace(search_strs[j], '$$$$000')
							search_strs[i] = search_strs[i].replace(search_strs[i], '$$$$111')
					else:
						if (search_strs[j - 1].strip()[-2:] != "||" and search_strs[j - 1].strip()[-2:] != "&&") and \
								(search_strs[i + 1].strip()[:2] != "||" and search_strs[i + 1].strip()[:2] != "&&"):
							search_strs[j] = search_strs[j].replace(search_strs[j], '$$$$000')
							search_strs[i] = search_strs[i].replace(search_strs[i], '$$$$111')
				else:
					search_strs[i] = search_strs[i].replace(search_strs[i], '$$$$111')
		for t in temp:
			m, bracket = t
			search_strs[m] = search_strs[m].replace(search_strs[m], '$$$$000')
		return ''.join(search_strs)

	def replace_bracket(self, expression_list):
		ret = []
		for item in expression_list:
			ret.append(item.replace('$$$$000', '(').replace('$$$$111', ')'))
		return ret

	def double_quote_format_match(self, szRuleExp):
		index = 0
		indexPrev = -1
		szFakeRuleExp = ''
		mapSeedRules = {}
		try:
			szRuleExp = self.adjust_rule_symbols(szRuleExp=szRuleExp)
			nSize = len(szRuleExp)
			while index < nSize:
				if szRuleExp[index] == '"':
					if index == 0:
						indexPrev = index
						szFakeRuleExp = szFakeRuleExp + szRuleExp[index]
					else:
						if szRuleExp[index - 1] == '\\':
							pass
						else:
							if indexPrev == -1:
								indexPrev = index
								szFakeRuleExp = szFakeRuleExp + szRuleExp[index]
							else:
								nCount = len(mapSeedRules)
								szKey = '$' + str(nCount)
								szValue = szRuleExp[indexPrev + 1:index]
								mapSeedRules[szKey] = szValue
								szFakeRuleExp = szFakeRuleExp + szKey + szRuleExp[index]
								indexPrev = -1
					index = index + 1
				else:
					if indexPrev == -1:
						szFakeRuleExp = szFakeRuleExp + szRuleExp[index]
					index = index + 1

		except Exception as e:
			mapSeedRules = {}
			szFakeRuleExp = ''
			if self.oLogger:
				self.oLogger.error(traceback.format_exc(e))
				self.oLogger.error('PostSuffix: Double quote format match failed, szRuleExp=[%s]' % (szRuleExp))
		return szFakeRuleExp, mapSeedRules

	def is_double_quote_suffix_match(self):
		return True if ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_PARSE_SUFFIX_TYPE == ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_PARSE_SUFFIX_DOUBLE_QUOTE else False

	def is_bracket_suffix_match(self):
		return True if ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_PARSE_SUFFIX_TYPE == ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_PARSE_SUFFIX_BRACKET else False


class OperatorMatch(object):
	def __init__(self, src, szRuleExp, split=':', oLogger=None):
		self.src = src
		self.oLogger = oLogger
		self.rule_list, self.mapSeedRules = self.GetExpSuffixList(szRuleExp)
		self.split = split

	def GetExpSuffixList(self, szRuleExp):
		oPostsuffix = PostSuffix(self.oLogger)
		lstSuffix, mapSeedRules = oPostsuffix.suffix(szRuleExp, return_type='list')
		# print '后缀表达式------', lstSuffix
		# print 'value mapping------', mapSeedRules
		return lstSuffix, mapSeedRules

	def ReplaceIgnoreSymbols(self, v):
		v = v.strip()
		if v.startswith('"'):
			v = v[1:]
		if v.endswith('"'):
			v = v[:-1]
		return v

	def MatchSingleRule(self, rule):
        
		isMatch = False
		blFilterRuleItem, iOperator, szRuleKey, szRuleVal = self.SplitRuleItem(szRuleItem=rule)
		if not blFilterRuleItem:
			data = self.GetHayStackData(szKey=szRuleKey)
			#print(data)
			if data:
				isMatch = self.MatchSingleRuleProc(szRuleVal=szRuleVal, szData=data, iOperator=iOperator)
			else:
				isMatch = False
		else:
			isMatch = False
		return isMatch

	def IsDoubleQuoteSuffixMatch(self):
		return True if ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_PARSE_SUFFIX_TYPE == ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_PARSE_SUFFIX_DOUBLE_QUOTE else False

	def IsBracketSuffixMatch(self):
		return True if ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_PARSE_SUFFIX_TYPE == ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_PARSE_SUFFIX_BRACKET else False

	def SplitRuleItem(self, szRuleItem, szSplit=ProbeDefine.PROBE_SCAN_FP_RULE_SPLIT_SYMBOL):
		szRuleItemKey = None
		szRuleItemVal = None
		blFilterRuleItem = True
		iOperator = ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_EQUAL
		try:
			lstRuleItem = szRuleItem.split(szSplit, 1)
			if lstRuleItem and len(lstRuleItem) == ProbeDefine.PROBE_SCAN_FP_RULE_ITEM_OPERAND_NUMBER:
				szRuleItemKey = lstRuleItem[0]
				iOperator = self.GetOperatorFromRule(szRuleItem=szRuleItemKey)
				szRuleItemKey = self.ReplaceInvalidSymbolsOfKey(szValue=szRuleItemKey)
				if szRuleItemKey:
					szRuleItemVal = lstRuleItem[1]
					iOperator = iOperator | self.GetOperatorFromRule(szRuleItem=szRuleItemVal, blKey=False)
					szRuleItemVal = self.ReplaceInvalidSymbolsOfValue(szValue=szRuleItemVal)
					szRuleItemVal = self.GetActualRuleValue(szRuleValue=szRuleItemVal)
					if szRuleItemVal:
						blFilterRuleItem = False
					else:
						blFilterRuleItem = True
				else:
					blFilterRuleItem = True
			else:
				blFilterRuleItem = True
		except Exception as e:
			iOperator = ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_EQUAL
			blFilterRuleItem = True
			szRuleItemKey = None
			szRuleItemVal = None
			if self.oLogger:
				self.oLogger.error(traceback.format_exc(e))
				self.oLogger.error('OperatorMatch: Split the item of rule failed, szRuleItem=[%s], szSpiltSymbol=[%s]' % (szRuleItem, szSplit))
		return blFilterRuleItem, iOperator, szRuleItemKey, szRuleItemVal

	def GetOperatorFromRule(self, szRuleItem, blKey=True):
		szRuleItem = szRuleItem.strip()
		iOperator = ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_EQUAL
		if blKey:
			if szRuleItem.endswith(ProbeDefine.PROBE_SCAN_FP_RULE_SPLIT_NOT_EQUAL_SYMBOL):
				iOperator = ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_NOT_EQUAL
			elif szRuleItem.endswith(ProbeDefine.PROBE_SCAN_FP_RULE_SPLIT_REGEX_SYMBOL):
				iOperator = ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_REGULAR_EXPRESSION
			else:
				iOperator = ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_EQUAL
		else:
			if szRuleItem.startswith(ProbeDefine.PROBE_SCAN_FP_RULE_SPLIT_NOT_EQUAL_SYMBOL):
				iOperator = ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_NOT_EQUAL
			elif szRuleItem.startswith(ProbeDefine.PROBE_SCAN_FP_RULE_SPLIT_ABSOLUTE_EQUAL_SYMBOL):
				iOperator = ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_ABSOLUTE_EQUAL
			elif szRuleItem.startswith(ProbeDefine.PROBE_SCAN_FP_RULE_SPLIT_REGEX_SYMBOL):
				iOperator = ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_REGULAR_EXPRESSION
			else:
				iOperator = ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_EQUAL
		return iOperator

	def ReplaceInvalidSymbolsOfKey(self, szValue):
		szValue = szValue.strip()
		for szSymbol in ProbeDefine.PROBE_SCAN_FP_RULE_KEY_INVALID_SYMBOLS_LIST:
			if szSymbol in szValue:
				szValue = szValue.replace(szSymbol, '')
			else:
				continue
		szValue = self.ReplaceIgnoreSymbols(szValue)
		return szValue

	def ReplaceInvalidSymbolsOfValue(self, szValue):
		szValue = szValue.strip()
		for szSymbol in ProbeDefine.PROBE_SCAN_FP_RULE_VALUE_INVALID_SYMBOLS_LIST:
			if szValue.startswith(szSymbol):
				szValue = szValue.replace(szSymbol, '', 1)
			else:
				continue
		szValue = self.ReplaceIgnoreSymbols(szValue)
		return szValue

	def AdjustRuleValue(self, szValue):
		szAdjustValue = szValue
		if szAdjustValue and len(ProbeDefine.PROBE_SCAN_FP_MPM_PATTERN_ADJUST_SYMBOLS) > 0:
			try:
				szAdjustValue = json.dumps(szAdjustValue, ensure_ascii=False)
				for oSymbol in ProbeDefine.PROBE_SCAN_FP_MPM_PATTERN_ADJUST_SYMBOLS:
					szOrg = oSymbol.get('org', '\\\\\\"')
					szDst = oSymbol.get('dst', '"')
					szAdjustValue = szAdjustValue.replace(szOrg, szDst).strip('"')
			except Exception as e:
				if self.oLogger:
					self.oLogger.error(traceback.format_exc(e))
					self.oLogger.error('OperatorMatch: Adjust rule value=[%s] failed.' % (szValue))
				szAdjustValue = szValue
		else:
			szAdjustValue = szValue
		return szAdjustValue

	def GetHayStackData(self, szKey):
		v = ''
		data = self.src.get('data', {})
		if 'header' in szKey:
			v = data.get('header', '')
		elif 'title' in szKey:
			v = data.get('title', '')
		elif 'body' in szKey:
			v = data.get('body', '')
		elif 'port' in szKey:
			v = str(data.get('port',''))
		elif 'banner' in szKey:
			v = data.get('banner', '')
		elif 'service' in szKey:
			v = data.get("service", "")
		elif 'protocol' in szKey:
			v = data.get("service", "")
		elif 'server' in szKey:
			v = data.get("server", "")
		else:
			v = data.get('banner', '')
		return v

	def MatchSingleRuleProc(self, szRuleVal, szData, iOperator):
		isMatch = False
		if iOperator & ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_ABSOLUTE_EQUAL:
			isMatch = self.OperatorAbsoluteEqualMatch(szRuleVal=szRuleVal, szData=szData)
		elif iOperator & ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_NOT_EQUAL:
			isMatch = self.OperatorNotEqualMatch(szRuleVal=szRuleVal, szData=szData)
		elif iOperator & ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_REGULAR_EXPRESSION:
			isMatch = self.OperatorRegexMatch(szRuleVal=szRuleVal, szData=szData)
		elif iOperator & ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_EQUAL:
			isMatch = self.OperatorEqualMatch(szRuleVal=szRuleVal, szData=szData)
		else:
			isMatch = self.OperatorEqualMatch(szRuleVal=szRuleVal, szData=szData)
		return isMatch

	def GetActualRuleValue(self, szRuleValue):
		szActualRuleValue = szRuleValue
		if self.IsDoubleQuoteSuffixMatch():
			szActualRuleValue = self.mapSeedRules.get(szRuleValue, '')
		else:
			szActualRuleValue = szRuleValue
		szActualRuleValue = self.AdjustRuleValue(szValue=szActualRuleValue)
		return szActualRuleValue

	def OperatorEqualMatch(self, szRuleVal, szData):
		return True if szRuleVal in szData else False

	def OperatorAbsoluteEqualMatch(self, szRuleVal, szData):
		return True if szRuleVal == szData else False

	def OperatorNotEqualMatch(self, szRuleVal, szData):
		return True if szRuleVal not in szData else False

	def OperatorRegexMatch(self, szRuleVal, szData):
		oRegRst = None
		oRegex = re.compile(szRuleVal)
		try:
			oRegRst = oRegex.search(str(szData))
		except Exception as e:
			if self.oLogger:
				self.oLogger.error(traceback.format_exc(e))
				self.oLogger.error('OperatorMatch: Calcualte regex expression failed, szData=[%s], szRegex=[%s]' % (szData, szRuleVal))
			oRegRst = None
		return True if oRegRst else False

	def IsMatch2Operand(self, m, opt):
		if opt == '&&':
			if m:
				return True
		elif opt == '||':
			if not m:
				return True
		return False

	def CalculateRuleExp(self, m1, m2, opt):
		if opt == '&&':
			return m1 and m2
		elif opt == '||':
			return m1 or m2

	def MatchRule(self, rule):
		if isinstance(rule, str) or isinstance(rule, unicode):
			is_match = self.MatchSingleRule(rule)
		elif isinstance(rule, list):
			is_match = self.CalculateRule(rule_list=rule)
		else:
			is_match = False
		return is_match

	def CalculateRule(self, rule_list):
		v1 = rule_list[0]
		m1 = self.MatchRule(v1)
		if len(rule_list) > 1:
			v2 = rule_list[1]
			opt = rule_list[2]
			if self.IsMatch2Operand(m1, opt) and v2:
				m2 = self.MatchRule(v2)
				return self.CalculateRuleExp(m1, m2, opt)
			else:
				return m1
		else:
			return m1

	def Calculate(self):
		blMatch = False
		try:
			blMatch = self.CalculateRule(rule_list=self.rule_list)
			if self.oLogger:
				self.oLogger.debug('OperatorMatch: Calculate the list of rules result stats: blMatch=[%s] lstRules=%s' % (blMatch, self.rule_list))
		except Exception as e:
			blMatch = False
			if self.oLogger:
				self.oLogger.error(traceback.format_exc(e))
				self.oLogger.error('OperatorMatch: Calculate the list of rules failed, lstRules=%s' % (self.rule_list))
		return blMatch


class CyberCalculate(OperatorMatch):
	def __init__(self, szHayStack, szRule, szSplit=None, oLogger=None):
		super(CyberCalculate, self).__init__(src=szHayStack, szRuleExp=szRule, split=szSplit, oLogger=oLogger)
		self.szRule = szRule

	def GetHayStackData(self, szKey):
		szVal = ''
		if szKey and szKey in self.src:
			szVal = self.src.get(szKey, '')
		else:
			szVal = self.src.get(ProbeDefine.PROBE_SCAN_FP_RULE_CALCULATE_HAYSTACK_UNIVERSAL_KEY, '')
		if not szVal:
			szVal = super(CyberCalculate, self).GetHayStackData(szKey)
		else:
			pass
		return szVal

	def OperatorEqualMatch(self, szRuleVal, szData):
		return super(CyberCalculate, self).OperatorEqualMatch(szRuleVal=szRuleVal, szData=szData)

	def OperatorAbsoluteEqualMatch(self, szRuleVal, szData):
		return super(CyberCalculate, self).OperatorAbsoluteEqualMatch(szRuleVal=szRuleVal, szData=szData)

	def OperatorNotEqualMatch(self, szRuleVal, szData):
		return super(CyberCalculate, self).OperatorNotEqualMatch(szRuleVal=szRuleVal, szData=szData)

	def OperatorRegexMatch(self, szRuleVal, szData):
		return super(CyberCalculate, self).OperatorRegexMatch(szRuleVal=szRuleVal, szData=szData)

	def Calculate(self):
		blMatch = False
		try:
			blMatch = super(CyberCalculate, self).Calculate()
			if self.oLogger:
				self.oLogger.debug('CyberCalculate: Calculate FP rule result stats: blMatch=[%s],szHayStack=[%s],szRule=[%s]' % (blMatch, self.src, self.szRule))
		except Exception as e:
			blMatch = False
			if self.oLogger:
				self.oLogger.error(traceback.format_exc(e))
				self.oLogger.error('CyberCalculate: Calculate FP rule failed, szHayStack=[%s],szRule=[%s]' % (self.src, self.szRule))
		return blMatch


if __name__ == '__main__':
	# szRule='title="NVR Station && Web" || (body="location=\\"index_cn||.htm\\";" && body="if(SysLan == \\"zh-cn")|| title=="WMS browse NVR"'
	# szRule = 'title="Powered by CmsEasy" || header="http://www.cmseasy.cn/service_1.html" || body="content=\\"CmsEasy"'
	# oOperand = {'title': "Web Server Error NVR Station && Web Report home 1234567 WMS browse NVR", 'body': "aaassl1ocation=\"index_cn||.htm\";if(SysLan == \"zh-cn"}
	# oCyberCalc = CyberCalculate(szHayStack=oOperand, szRule=szRule, szSplit='=')
	# blMatch = oCyberCalc.Calculate()
	# szRule = 'title!="te\\"st"||header="Server: nginx/1.10.3 (Ubuntu)"'
	# oOperand = {"status": "up", "trace": [], "tags": [], "ip": "661214482", "hostname": "", "mask": "", "gateway": "",
	#      "port": 80,
	#      "mac": "", "os_family": "Linux", "data": {"status": "open",
	#                                                "detail_text": "detail.http.status : 200\ndetail.http.body : \n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n<html xmlns=\"http://www.w3.org/1999/xhtml\">\n  <!--\n    Modified from the Debian original for Ubuntu\n    Last updated: 2014-03-19\n    See: https://launchpad.net/bugs/1288690\n  -->\n  <head>\n    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />\n    <title>Apache2 Ubuntu Default Page: It works</title>\n    <style type=\"text/css\" media=\"screen\">\n  * {\n    margin: 0px 0px 0px 0px;\n    padding: 0px 0px 0px 0px;\n  }\n\n  body, html {\n    padding: 3px 3px 3px 3px;\n\n    background-color: #D8DBE2;\n\n    font-family: Verdana, sans-serif;\n    font-size: 11pt;\n    text-align: center;\n  }\n\n  div.main_page {\n    position: relative;\n    display: table;\n\n    width: 800px;\n\n    margin-bottom: 3px;\n    margin-left: auto;\n    margin-right: auto;\n    padding: 0px 0px 0px 0px;\n\n    border-width: 2px;\n    border-color: #212738;\n    border-style: solid;\n\n    background-color: #FFFFFF;\n\n    text-align: center;\n  }\n\n  div.page_header {\n    height: 99px;\n    width: 100%;\n\n    background-color: #F5F6F7;\n  }\n\n  div.page_header span {\n    margin: 15px 0px 0px 50px;\n\n    font-size: 180%;\n    font-weight: bold;\n  }\n\n  div.page_header img {\n    margin: 3px 0px 0px 40px;\n\n    border: 0px 0px 0px;\n  }\n\n  div.table_of_contents {\n    clear: left;\n\n    min-width: 200px;\n\n    margin: 3px 3px 3px 3px;\n\n    background-color: #FFFFFF;\n\n    text-align: left;\n  }\n\n  div.table_of_contents_item {\n    clear: left;\n\n    width: 100%;\n\n    margin: 4px 0px 0px 0px;\n\n    background-color: #FFFFFF;\n\n    color: #000000;\n    text-align: left;\n  }\n\n  div.table_of_contents_item a {\n    margin: 6px 0px 0px 6px;\n  }\n\n  div.content_section {\n    margin: 3px 3px 3px 3px;\n\n    background-color: #FFFFFF;\n\n    text-align: left;\n  }\n\n  div.content_section_text {\n    padding: 4px 8px 4px 8px;\n\n    color: #000000;\n    font-size: 100%;\n  }\n\n  div.content_section_text pre {\n    margin: 8px 0px 8px 0px;\n    padding: 8px 8px 8px 8px;\n\n    bord\ndetail.http.server : nginx/1.10.3 (Ubuntu)\ndetail.http.conttype :  text/html\ndetail.http.title : Apache2 Ubuntu Default Page: It works\n",
	#                                                "product": "nginx", "protocol": "tcp",
	#                                                "xmap_text": "xmap.http-server-header : nginx/1.10.3 (Ubuntu)\n",
	#                                                "service": "http", "title": "title te\"st", "os_score": 93,
	#                                                "detail": {
	# 	                                               "http": {"status": 200,
	# 	                                                        "body": "\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n<html xmlns=\"http://www.w3.org/1999/xhtml\">\n  <!--\n    Modified from the Debian original for Ubuntu\n    Last updated: 2014-03-19\n    See: https://launchpad.net/bugs/1288690\n  -->\n  <head>\n    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />\n    <title>Apache2 Ubuntu Default Page: It works</title>\n    <style type=\"text/css\" media=\"screen\">\n  * {\n    margin: 0px 0px 0px 0px;\n    padding: 0px 0px 0px 0px;\n  }\n\n  body, html {\n    padding: 3px 3px 3px 3px;\n\n    background-color: #D8DBE2;\n\n    font-family: Verdana, sans-serif;\n    font-size: 11pt;\n    text-align: center;\n  }\n\n  div.main_page {\n    position: relative;\n    display: table;\n\n    width: 800px;\n\n    margin-bottom: 3px;\n    margin-left: auto;\n    margin-right: auto;\n    padding: 0px 0px 0px 0px;\n\n    border-width: 2px;\n    border-color: #212738;\n    border-style: solid;\n\n    background-color: #FFFFFF;\n\n    text-align: center;\n  }\n\n  div.page_header {\n    height: 99px;\n    width: 100%;\n\n    background-color: #F5F6F7;\n  }\n\n  div.page_header span {\n    margin: 15px 0px 0px 50px;\n\n    font-size: 180%;\n    font-weight: bold;\n  }\n\n  div.page_header img {\n    margin: 3px 0px 0px 40px;\n\n    border: 0px 0px 0px;\n  }\n\n  div.table_of_contents {\n    clear: left;\n\n    min-width: 200px;\n\n    margin: 3px 3px 3px 3px;\n\n    background-color: #FFFFFF;\n\n    text-align: left;\n  }\n\n  div.table_of_contents_item {\n    clear: left;\n\n    width: 100%;\n\n    margin: 4px 0px 0px 0px;\n\n    background-color: #FFFFFF;\n\n    color: #000000;\n    text-align: left;\n  }\n\n  div.table_of_contents_item a {\n    margin: 6px 0px 0px 6px;\n  }\n\n  div.content_section {\n    margin: 3px 3px 3px 3px;\n\n    background-color: #FFFFFF;\n\n    text-align: left;\n  }\n\n  div.content_section_text {\n    padding: 4px 8px 4px 8px;\n\n    color: #000000;\n    font-size: 100%;\n  }\n\n  div.content_section_text pre {\n    margin: 8px 0px 8px 0px;\n    padding: 8px 8px 8px 8px;\n\n    bord",
	# 	                                                        "server": "nginx/1.10.3 (Ubuntu)",
	# 	                                                        "conttype": " text/html",
	# 	                                                        "title": "Apache2 Ubuntu Default Page: It works"}},
	#                                                "version": "1.10.3",
	#                                                "banner": "HTTP/1.1 200 OK\r\nServer: nginx/1.10.3 (Ubuntu)\r\nDate: Tue, 30 Jul 2019 12:13:10 GMT\r\nContent-Type: text/html\r\nContent-Length: 11321\r\nLast-Modified: Thu, 13 Sep 2018 07:22:40 GMT\r\nConnection: keep-alive\r\nETag: \"5b9a1040-2c39\"\r\nAccept-Ranges: bytes",
	#                                                "port": 80, "xmap": {"http-server-header": "nginx/1.10.3 (Ubuntu)"}},
	#      "device_type": "\u8ba1\u7b97\u673a\u7ec8\u7aef", "os_score": 93, "device": "\u8ba1\u7b97\u673a\u7ec8\u7aef",
	#      "ip_str": "39.105.85.18", "os": "Linux 4.4",
	#      "cpes": ["cpe:/a:igor_sysoev:nginx:1.10.3", "cpe:/o:linux:linux_kernel"], "manufacturer": ""}
	szRule = 'body="JavaScript"'
	oOperand= {"data" : {'body': u'\r\n<script language="JavaScript"> \r\n    var authen_result =\'YES\';\r\n    if(authen_result==\'YES\' ){\r\n        window.document.location = \'/license!getExpireDateOfDays.action\';\r\n    }else{\r\n   \t\twindow.document.location = \'/license!reReadLicense.action\';\r\n        //window.document.location = \'/modules/sys/license_upload.jsp\';\r\n    }\r\n</script>', 'service': u'http', 'title': '1', 'protocal': u'http', 'header': 'Apache-Coyote/1.1JSESSIONID=7B8B9B3F38A24C41D943511AD4DD6D80; Path=/text/html;charset=utf-8340Fri, 29 Jan 2021 06:18:27 GMT', 'port': 81}}
	oCyberCalc = CyberCalculate(szHayStack=oOperand, szRule=szRule, szSplit='=')
	blMatch = oCyberCalc.Calculate()
	print(blMatch)
	# postSuffix = PostSuffix()
	# print postSuffix.suffix('header="Windows/x86"')
	# pass