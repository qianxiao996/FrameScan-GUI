# coding=utf-8


PROBE_SCAN_TYPE_COUNTS = 3
PROBE_SCAN_TYPE_CYBER_SCAN = 0
PROBE_SCAN_TYPE_NMAP_SCAN = 1
PROBE_SCAN_TYPE_DEEP_SCAN = 2

PROBE_SCAN_TYPE_CYBER_SCAN_STRING = 'Probe_Cyber_Scan'
PROBE_SCAN_TYPE_NMAP_SCAN_STRING = 'Probe_Nmap_Scan'
PROBE_SCAN_TYPE_DEEP_SCAN_STRING = 'Probe_Deep_Scan'

PROBE_SCAN_ENUM_STATUS_CODE_IDLE = 0x01
PROBE_SCAN_ENUM_STATUS_CODE_START_UP = 0x02
PROBE_SCAN_ENUM_STATUS_CODE_RUNNING = 0x04
PROBE_SCAN_ENUM_STATUS_CODE_COMPLETED = 0x08
PROBE_SCAN_ENUM_STATUS_CODE_SUCCESS = 0x10
PROBE_SCAN_ENUM_STATUS_CODE_FAILURE = 0x20
PROBE_SCAN_ENUM_STATUS_CODE_CANCELED = 0x40
PROBE_SCAN_ENUM_STATUS_CODE_TIMEOUT = 0x80

PROBE_SCAN_STRING_STATUS_CODE_IDLE = 'Idle'
PROBE_SCAN_STRING_STATUS_CODE_START_UP = 'StartUp'
PROBE_SCAN_STRING_STATUS_CODE_RUNNING = 'Running'
PROBE_SCAN_STRING_STATUS_CODE_COMPLETED = 'Completed'
PROBE_SCAN_STRING_STATUS_CODE_SUCCESS = 'Success'
PROBE_SCAN_STRING_STATUS_CODE_FAILURE = 'Failure'
PROBE_SCAN_STRING_STATUS_CODE_CANCELED = 'Canceled'
PROBE_SCAN_STRING_STATUS_CODE_TIMEOUT = 'TimeOut'


PROBE_SCAN_CONFIG_REPORT_STATUS_COMPLETED = 'completed'
PROBE_SCAN_CONFIG_REPORT_STATUS_CANCELED = 'canceled'
PROBE_SCAN_CONFIG_REPORT_STATUS_ERROR = 'error'

PROBE_SCAN_CONFIG_RESULT_DATA_COMPRESS_TAG = True

PROBE_SCAN_CONFIG_JOB_DSC_FILE_NAME = 'jd.dat'
PROBE_SCAN_CONFIG_JOB_LOG_FILE_NAME = 'log.dat'
PROBE_SCAN_CONFIG_JOB_LOCK_FILE_NAME = 'jd.lck'
PROBE_SCAN_CONFIG_JOB_RESULT_FILE_NAME = 'result.json'
PROBE_SCAN_CONFIG_JOB_NMAP_DIRECTORY_NAME = 'nmap/'
PROBE_SCAN_CONFIG_JOB_DEEP_DIRECTORY_NAME = 'deep/'

PROBE_SCAN_ANALYZE_DEPPORT_DIRECTORY = '/rayos/app/tools/depprot'
PROBE_SCAN_ANALYZE_PORT_FILE_NAME = 'config/analyse_port.conf'
PROBE_SCAN_ANALYZE_SERVICE_FILE_NAME = 'config/analyse_service.conf'
PROBE_SCAN_CORRECT_OS_FILE_NAME = 'config/need_modify_os'
PROBE_SCAN_FP_MPM_RULE_KEYS_FILE_NAME = 'config/FP_Rule_Keys.conf'
PROBE_SCAN_DEEP_SCAN_SO_LIBRARY_DEPPROT = 'lib/libdepprot.so'
PROBE_SCAN_FP_CVE_CPE_DATABASE_NAME = 'db/cve_cpe.db'
PROBE_SCAN_FP_CVE_CPE_TABLE_NAME = 'cve_cpe'
PROBE_SCAN_FP_CVE_CPE_APP_TABLE_NAME = 'cve_cpe_a'
PROBE_SCAN_FP_CVE_CPE_OS_TABLE_NAME = 'cve_cpe_o'
PROBE_SCAN_FP_CVE_CPE_HW_TABLE_NAME = 'cve_cpe_h'
PROBE_SCAN_FINGER_PRINT_DATABASE_NAME = 'db/finger_db.db'
PROBE_SCAN_FINGER_PRINT_TABLE_NAME = 'finger'
PROBE_SCAN_AUTOMATON_SERIALIZE_FILES_DIRECTORY = 'pkl'
PROBE_SCAN_AUTOMATON_SERIALIZE_FILES_EXTENSION = '.pkl'

PROBE_SCAN_ANALYZE_SERVICE_APPEND_TCPWRAPPED = 'tcpwrapped'
PROBE_SCAN_ANALYZE_SERVICE_APPEND_UNKNOWN = 'unknown'

PROBE_SCAN_PLUGIN_NMAP = '/rayos/app/nmap/bin/nmap'

PROBE_SCAN_DATA_TYPE_FIG = 10
PROBE_SCAN_TASK_TYPE_FIG = 10

PROBE_SCAN_FAKE_SERVICES_LIST = ['tcpwrapped', 'unknown']

VERIFY_TUNNEL_SEVICE = ['imap', 'smtp', 'pop3', 'imaps', 'smtps', 'pop3s']
PROBE_SCAN_TUNNEL_SERVICE_SSL = '-ssl'
PROBE_SCAN_TUNNEL_SERVICE_TLS = '-tls'

PROBE_SCAN_NMAP_OUTPUT_FILE_TYPE_XML = 0
PROBE_SCAN_NMAP_OUTPUT_FILE_TYPE_JSON = 1
PROBE_SCAN_NMAP_OUTPUT_FILE_POSTFIX_EXTENSION = '.xml'
PROBE_SCAN_DEEP_OUTPUT_FILE_POSTFIX_EXTENSION = '.json'

PROBE_SCAN_PROTOCOL_TCP = 'tcp'
PROBE_SCAN_PROTOCOL_UDP = 'udp'
PROBE_SCAN_IP_TYPE_V6 = '6'
PROBE_SCAN_IP_TYPE_V4 = '4'
PROBE_SCAN_IPV4_FULL_LENGTH = 10
PROBE_SCAN_IPV6_FULL_LENGTH = 40
PROBE_SCAN_PORT_FULL_LENGTH = 6

PROBE_SCAN_NMAP_COMMAND_TYPE_GENERAL = 0
PROBE_SCAN_NMAP_COMMAND_TYPE_OS = 1
PROBE_SCAN_NMAP_COMMAND_TYPE_SERVICE = 2

PROBE_SCAN_NMAP_COMMAND_TYPE_STRING_GENERAL = 'NMAP_COMMAND_GENERAL'
PROBE_SCAN_NMAP_COMMAND_TYPE_STRING_OS = 'NMAP_COMMAND_OS'
PROBE_SCAN_NMAP_COMMAND_TYPE_STRING_SERVICE = 'NMAP_COMMAND_SERVICE'

PROBE_SCAN_DATA_MERGE_TYPE_CYBER = 0
PROBE_SCAN_DATA_MERGE_TYPE_NMAP = 1
PROBE_SCAN_DATA_MERGE_TYPE_DEEP = 2
PROBE_SCAN_DATA_MERGE_TYPE_VULN = 3
PROBE_SCAN_DATA_MERGE_TYPE_FP_MATCH = 4
PROBE_SCAN_DATA_MERGE_TYPE_COMMON = 5

PROBE_SCAN_DATA_MERGE_TYPE_STRING_CYBER = 'CYBER_DATA_MERGE'
PROBE_SCAN_DATA_MERGE_TYPE_STRING_NMAP = 'NMAP_DATA_MERGE'
PROBE_SCAN_DATA_MERGE_TYPE_STRING_DEEP = 'DEEP_DATA_MERGE'
PROBE_SCAN_DATA_MERGE_TYPE_STRING_VULN = 'VULN_DATA_MERGE'
PROBE_SCAN_DATA_MERGE_TYPE_STRING_FP_MATCH = 'FP_MATCH_DATA_MERGE'
PROBE_SCAN_DATA_MERGE_TYPE_STRING_COMMON = 'COMMON_DATA_MERGE'


PROBE_SCAN_XMAP_FAKE_DATA_SUFFIX_SYMBOL = '?'
NMAP_DEVICE_OBJ = {	
					'webcam': 	{
									'CateMain': {
													'en': 'Network Camera',
													'zh': '网络摄像头'
												},
									'CateSub': 	{
													'en': 'Webcam'
												}
								},				
					'security-misc': 	{
											'CateMain':	{
															'en': 'Network Security',
															'zh': '安全防护设备'
														},
											'CateSub':	{
															'en': 'Security Misc'
														}
										}, 		
					'game console':	{
										'CateMain':	{
														'en': 'IoT',
														'zh': '物联网设备'
													},
										'CateSub':	{
														'en': 'Game Console'
													}										
									},
					'switch': 	{
									'CateMain':	{
													'en': 'Router & Switch',
													'zh': '路由交换设备'
												},
									'CateSub':	{
													'en': 'Switch'
												}		
								},
					'router':	{
									'CateMain':	{
													'en': 'Router & Switch',
													'zh': '路由交换设备'
												},
									'CateSub':	{
													'en': 'Router'
												}		
								},
					'print server': {
										'CateMain':	{
														'en': 'Network Printer',
														'zh': '网络打印机'
													},
										'CateSub':	{
														'en': 'Printer Server'
													}	
									}, 		
					'bridge': 	{
									'CateMain':	{
													'en': 'Router & Switch',
													'zh': '路由交换设备'
												},
									'CateSub':	{
													'en': 'Bridge'
												}	
								}, 			
					'specialized': 	{
										'CateMain':	{
														'en': 'Device Misc',
														'zh': '其它网络设备'
													},
										'CateSub':	{
														'en': 'Specialized'
													}	
									},
					'firewall': {
									'CateMain':	{
													'en': 'Router & Switch',
													'zh': '路由交换设备'
												},
									'CateSub':	{
													'en': 'Firewall'
												}	
								}, 			
					'PBX': 	{
								'CateMain':	{
												'en': 'VoIP Device',
												'zh': '网络电话'
											},
								'CateSub':	{
												'en': 'PBX'
											}	
							}, 
					'WAP':	{
								'CateMain':	{
												'en': 'Router & Switch',
												'zh': '路由交换设备'
											},
								'CateSub':	{
												'en': 'Wireless AP'
											}	
							}, 
					'PDA': 	{
								'CateMain':	{
												'en': 'Smart Mobile Terminal',
												'zh': '智能移动终端'
											},
								'CateSub':	{
												'en': 'PDA'
											}	
							},
					'power-device': {
										'CateMain':	{
														'en': 'IoT',
														'zh': '物联网设备'
													},
										'CateSub':	{
														'en': 'Power Device'
													}	
									}, 	
					'storage-misc': {
										'CateMain':	{
														'en': 'Network Storage',
														'zh': '网络存储设备'
													},
										'CateSub':	{
														'en': 'Storage Misc'
													}	
									}, 	
					'VoIP phone': 	{
										'CateMain':	{
														'en': 'VoIP Device',
														'zh': '网络电话'
													},
										'CateSub':	{
														'en': 'IP Phone'
													}	
									},
					'terminal': {
									'CateMain':	{
													'en': 'Computer Terminal',
													'zh': '计算机终端'
												},
									'CateSub':	{
													'en': 'Thin Client'
												}	
								}, 		
					'load balancer': 	{
											'CateMain':	{
															'en': 'Load Balancer',
															'zh': '负载均衡设备'
														},
											'CateSub':	{
															'en': 'Load Balancer'
														}	
										}, 	
					'general purpose': 	{
											'CateMain':	{
															'en': 'Device Misc',
															'zh': '其它网络设备'
														},
											'CateSub':	{
															'en': 'Misc'
														}	
										},
					'VoIP adapter': {
										'CateMain':	{
														'en': 'VoIP Device',
														'zh': '网络电话'
													},
										'CateSub':	{
														'en': 'VoIP Adapter'
													}	
									}, 	
					'media device': {
										'CateMain':	{
														'en': 'IoT',
														'zh': '物联网设备'
													},
										'CateSub':	{
														'en': 'Media Device'
													}	
									}, 		
					'terminal server': 	{
											'CateMain':	{
															'en': 'Device Misc',
															'zh': '其它网络设备'
														},
											'CateSub':	{
															'en': 'Terminal Server'
														}	
										},
					'telecom-misc': {
										'CateMain':	{
														'en': 'Device Misc',
														'zh': '其它网络设备'
													},
										'CateSub':	{
														'en': 'Telecom'
													}	
									},  	
					'broadband router': {
											'CateMain':	{
															'en': 'Router & Switch',
															'zh': '路由交换设备'
														},
											'CateSub':	{
															'en': 'Router'
														}	
										}, 
					'printer': 	{
									'CateMain':	{
													'en': 'Network Printer',
													'zh': '网络打印机'
												},
									'CateSub':	{
													'en': 'Printer'
												}	
								},
					'remote management': 	{
												'CateMain':	{
																'en': 'IT Operations Management',
																'zh': '运维管理'
															},
												'CateSub':	{
																'en': 'Remote Management'
															}
											},
					'phone': 	{
									'CateMain':	{
													'en': 'Smart Mobile Terminal',
													'zh': '智能移动终端'
												},
									'CateSub':	{
													'en': 'Mobile Phone'
												}
								},
					'proxy server': {
										'CateMain':	{
														'en': 'Network Security',
														'zh': '安全防护设备'
													},
										'CateSub':	{
														'en': 'Proxy Server'
													}
									},
					'hub': {
								'CateMain':	{
												'en': 'Router & Switch',
												'zh': '路由交换设备'
											},
								'CateSub':	{
												'en': 'Hub'
											}
							},
					'power-misc':  {
										'CateMain':	{
														'en': 'IoT',
														'zh': '物联网设备'
													},
										'CateSub':	{
														'en': 'Power Misc'
													}
									},
					'HP printer':  {
										'CateMain':	{
														'en': 'Network Printer',
														'zh': '网络打印机'
													},
										'CateSub':	{
														'en': 'Printer'
													}
									},
					'broadand router': {
											'CateMain':	{
															'en': 'Router & Switch',
															'zh': '路由交换设备'
														},
											'CateSub':	{
															'en': 'Router'
														}
										},
					'specializied': {
										'CateMain':	{
														'en': 'Device Misc',
														'zh': '其它网络设备'
													},
										'CateSub':	{
														'en': 'Specialized'
													}
									}
				}

OS_NAME_TO_DEVICE_RULE_TYPE_REGEX = 1
OS_NAME_TO_DEVICE_RULE_TYPE_STATIC_MAPPING = 2
OS_NAME_TO_DEVICE_RULE_TYPE_STRING = 3
OS_NAME_TO_DEVICE_RULE_FILTER_MAPPING = {	'Apple':{	'rule': '(^Apple (?:i|Mac\s|mac|iPhone\s|iPad\s|iPod\s)?OS(?: X)?(?: Server)? [0-9]{1,4}(?:.[0-9]{1-4}){0,10}(?:\s\-|\s\()?.*)',
														'type': 1,
														'reset': False
													},
											'FreeBSD': {
														'rule': '(^FreeBSD [0-9]{1,4}(?:.[0-9]{1-4}){0,10}(?:\s\-|\s\()?.*)',
														'type': 1
													},
											'Android': {
														'rule': '(^Android [0-9]{1,4}(?:.[0-9]{1-4}){0,10}(?:\s\-|\s\()?.*)',
														'type': 1
													},
											'HP': {
														'rule': '(^HP(?:\-UX\sB\.|\sMPE\/iX|\sOpenVMS|\sTru64\sUNIX)\s?[0-9]{1,4}(?:.[0-9]{1-4}){0,10}(?:\s\-|\s\()?.*)',
														'type': 1
													},
											'IBM': {
														'rule': '(^IBM (?:AIX|i|(?:i5|z)\/OS|OS\/[0-9]{1,4})(?:\sAIX|\sWarp)?\s?[0-9]{1,4}(?:.[0-9]{1-4}){0,10}(?:\s\-|\s\()?.*)',
														'type': 1
													},
											'Linux': {
														'rule': '(^Linux [0-9]{1,4}(?:.[0-9]{1-4}){0,10}(?:\s\-|\s\()?)',
														'type': 2
													},
											'OpenWrt (': {
														'rule': 'linux',
														'type': 3
													},
											'Microsoft Windows': {
														'rule': 'microsoft',
														'type': 3
													},
											'MikroTik RouterOS': {
														'rule': 'mikrotik',
														'type': 3
													},
											'OpenBSD': {
														'rule': 'openbsd',
														'type': 3
											},
											'Sun Solaris': {
														'rule': 'sun',
														'type': 3
											},
											'VMware': {
														'rule': 'vmware',
														'type': 3
											},
											'VxWorks': {
														'rule': 'vxworks',
														'type': 3
											}

										}

PROBE_SCAN_SERVICE_RENAME_MAPPING = {
										'ms-wbt-server': 'rdp'
									}


PROBE_SCAN_OS_ACTIVE_STATUS_UP = 'up'
PROBE_SCAN_SERVICE_ACTIVE_STATUS_OPEN = 'open'
PROBE_SCAN_OS_INACTIVE_STATUS_LIST = ['down']
PROBE_SCAN_SERVICE_INACTIVE_STATUS_LIST = ['filtered','closed']
PROBE_SCAN_SERVICE_INACTIVE_STATUS_FILTERED = 'filtered'


PROBE_SCAN_RMAP_RETRY_COUNTS = 2
PROBE_SCAN_DEEP_PROTOCOL_RETRY_COUNTS = 1
PROBE_SCAN_DATA_MERGE_VULN_RETRY_COUNTS = 1
PROBE_SCAN_DATA_MERGE_COMMON_RETRY_COUNTS = 1
PROBE_SCAN_DATA_MERGE_FP_MATCH_RETRY_COUNTS = 1

PROBE_SCAN_TYPE_HOST_ACTIVE = 0
PROBE_SCAN_TYPE_PORT_ACTIVE = 1
PROBE_SCAN_TYPE_FINGER_PRINT = 2

PROBE_SCAN_TYPE_STRING_HOST_ACTIVE = 'PROBE_HOST_ACTIVE'
PROBE_SCAN_TYPE_STRING_PORT_ACTIVE = 'PROBE_PORT_ACTIVE'
PROBE_SCAN_TYPE_STRING_FINGER_PRINT = 'PROBE_FINGER_PRINT'


PROBE_SCAN_FPM_REQUEST_TAG = 'FPMSV1.0'
PROBE_SCAN_FPM_REQUEST_SCHEMA_1 = 1

PROBE_SCAN_FPM_RESPONSE_STATUS_IDLE = 0
PROBE_SCAN_FPM_RESPONSE_STATUS_SUCCESS = 1
PROBE_SCAN_FPM_RESPONSE_STATUS_FAILURE = 2
PROBE_SCAN_FPM_RESPONSE_STATUS_TIMEOUT = 3
PROBE_SCAN_FPM_RESPONSE_STATUS_CANCELED = 4
PROBE_SCAN_FPM_RESPONSE_STATUS_UNKNOWN = 5

PROBR_SCAN_FPM_MESSAGE_TERMINATE_STRING = '$#@$#@$#@$_MESSAGE_TERMINATE_&~*~&*&~*'

PROBE_SCAN_FPM_REQUEST_TYPE_INVALID = 0
PROBE_SCAN_FPM_REQUEST_TYPE_FP_MATCHED = 1
PROBE_SCAN_FPM_REQUEST_TYPE_PLUGIN_PROCESS = 2
PROBE_SCAN_FPM_REQUEST_TYPE_GET_SERVICE_STATUS = 3
PROBE_SCAN_FPM_REQUEST_TYPE_STRING_INVALID = 'FPM_REQUEST_INVALID'
PROBE_SCAN_FPM_REQUEST_TYPE_STRING_FP_MATCHED = 'FPM_REQUEST_FP_MATCHED'
PROBE_SCAN_FPM_REQUEST_TYPE_STRING_PLUGIN_PROCESS = 'FPM_REQUEST_PLUGIN_PROCESS'
PROBE_SCAN_FPM_REQUEST_TYPE_STRING_GET_SERVICE_STATUS = 'FPM_REQUEST_SERVICE_STATUS'

PROBE_SCAN_FPM_RESPONSE_TYPE_INVALID = 10000
PROBE_SCAN_FPM_RESPONSE_TYPE_FP_MATCHED = 10001
PROBE_SCAN_FPM_RESPONSE_TYPE_PLUGIN_PROCESS = 10002
PROBE_SCAN_FPM_RESPONSE_TYPE_GET_SERVICE_STATUS = 10003
PROBE_SCAN_FPM_RESPONSE_TYPE_STRING_INVALID = 'FPM_RESPONSE_INVALID'
PROBE_SCAN_FPM_RESPONSE_TYPE_STRING_FP_MATCHED = 'FPM_RESPONSE_FP_MATCHED'
PROBE_SCAN_FPM_RESPONSE_TYPE_STRING_PLUGIN_PROCESS = 'FPM_RESPONSE_PLUGIN_PROCESS'
PROBE_SCAN_FPM_RESPONSE_TYPE_STRING_GET_SERVICE_STATUS = 'FPM_RESPONSE_SERVICE_STATUS'

PROBE_SCAN_FP_TYPE_BASE = 0
PROBE_SCAN_FP_TYPE_GENERAL = PROBE_SCAN_FP_TYPE_BASE
PROBE_SCAN_FP_TYPE_PLUGIN = 10

PROBE_SCAN_FP_TYPE_STRING_BASE = 'FP_BASE'
PROBE_SCAN_FP_TYPE_STRING_GENERAL = 'FP_GENERAL'
PROBE_SCAN_FP_TYPE_STRING_PLUGIN = 'FP_PLUGIN'

PROBE_SCAN_FP_RULE_ITEM_OPERAND_NUMBER = 2
PROBE_SCAN_FP_RULE_SPLIT_SYMBOL = '='
PROBE_SCAN_FP_RULE_SPLIT_NOT_EQUAL_SYMBOL = '!'
PROBE_SCAN_FP_RULE_SPLIT_ABSOLUTE_EQUAL_SYMBOL = PROBE_SCAN_FP_RULE_SPLIT_SYMBOL
PROBE_SCAN_FP_RULE_SPLIT_REGEX_SYMBOL = '*'

PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_EQUAL = 0x1
PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_ABSOLUTE_EQUAL = 0x2
PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_NOT_EQUAL = 0x4
PROBE_SCAN_FP_RULE_CALCULATE_OPERATOR_SYMBOL_REGULAR_EXPRESSION = 0x8

PROBE_SCAN_FP_RULE_KEY_INVALID_SYMBOLS_LIST = [' ', '!', '?', '~','<','>','/',',','.','(', ')', '[',']','{','}','@','#','$','%','^','&','*','+','-','_','=']
PROBE_SCAN_FP_RULE_VALUE_INVALID_SYMBOLS_LIST = ['=','!', '*']
PROBE_SCAN_FP_RULE_CALCULATE_SYMBOLS = ['&&', '||']
PROBE_SCAN_FP_RULE_ITEM_FIELD_SYMBOL = 'SYMBOL'
PROBE_SCAN_FP_RULE_ITEM_FIELD_VALUE = 'VALUE'

PROBE_SCAN_FP_RULE_CALCULATE_PARSE_SUFFIX_BRACKET = 0
PROBE_SCAN_FP_RULE_CALCULATE_PARSE_SUFFIX_DOUBLE_QUOTE = 1
PROBE_SCAN_FP_RULE_CALCULATE_PARSE_SUFFIX_TYPE = PROBE_SCAN_FP_RULE_CALCULATE_PARSE_SUFFIX_DOUBLE_QUOTE

PROBE_SCAN_FP_RULE_CALCULATE_HAYSTACK_UNIVERSAL_KEY = 'xmap_text'


PROBE_SCAN_FP_BASE_RECORD_FIELDS_COUNTS = 3
PROBE_SCAN_FP_GENERAL_RECORD_FIELDS_COUNTS = PROBE_SCAN_FP_BASE_RECORD_FIELDS_COUNTS + 1
PROBE_SCAN_FP_PLUGIN_RECORD_FIELDS_COUNTS = PROBE_SCAN_FP_BASE_RECORD_FIELDS_COUNTS + 1

# BASE FP
PROBE_SCAN_FP_SELECT_FIELDS_STRING = 'id, finger_type, finger, pname'
PROBE_SCAN_FP_RECORD_FIELD_INDEX_ID = 0
PROBE_SCAN_FP_RECORD_FIELD_INDEX_TYPE = 1
PROBE_SCAN_FP_RECORD_FIELD_INDEX_RULE = 2


# FP FIELD VALUE
PROBE_SCAN_FP_RECORD_FIELD_INVALID_VALUE = -1

# GENERAL FP
PROBE_SCAN_FP_GENERAL_FIELD_INDEX_NAME = PROBE_SCAN_FP_RECORD_FIELD_INDEX_RULE + 1


# PLUGIN FP
PROBE_SCAN_FP_PLUGIN_FIELD_INDEX_NAME = PROBE_SCAN_FP_RECORD_FIELD_INDEX_RULE + 1


# Finger Print MPM define
PROBE_SCAN_FP_MPM_TYPE_MPM = 0
PROBE_SCAN_FP_MPM_TYPE_KMP = 1
PROBE_SCAN_FP_MPM_TYPE_AC = 2
PROBE_SCAN_FP_MPM_TYPE_WU = 3

PROBE_SCAN_FP_MPM_TYPE_STRING_MPM = 'PROBE_FP_MPM'
PROBE_SCAN_FP_MPM_TYPE_STRING_KMP = 'PROBE_FP_KPM'
PROBE_SCAN_FP_MPM_TYPE_STRING_AC = 'PROBE_FP_AC'
PROBE_SCAN_FP_MPM_TYPE_STRING_WU = 'PROBE_FP_WU'

PROBE_SCAN_FP_MPM_PATTERN_ADJUST_SYMBOLS = [
												{
													'org': '\\\\\\"',
													'dst': '"'
												}
											]

PROBE_SCAN_FP_MPM_AUTOMATON_LOADING_FROM_DISK = True

PROBE_SCAN_FP_MPM_MANAGER_KEYS_LIST = ['header', 'body', 'title', 'banner']
PROBE_SCAN_FP_MPM_MANAGER_KEY_LEGACY = 'legacy'

PROBE_SCAN_FP_MPM_SOURCE_FIELDS_INCLUDES = ['data.title', 'data.detail.header', 'data.detail.realm','data.detail.server','data.detail.body','data.detail.status', 'os_family','data.banner','data.protocol','data.port','data.service','data.product','data.detail.ssl.0.cert']
PROBE_SCAN_FP_MPM_RESULT_FIELD_RULEIDS = 'rids'
PROBE_SCAN_FPM_SERVER_ERROR_FIELD = 'ERROR'
PROBE_SCAN_FPM_SERVER_ERROR_STRING_VALUE = 'FP matched encountered exception'

PROBE_SCAN_FP_MERGE_VULN_RESULT_MAX_COUNTS = 500
PROBE_SCAN_FP_MERGE_VULN_RESULT_VALUEABLE_MAX_COUNTS = 450
PROBE_SCAN_FP_VULN_CVSS2_LOW_LIMIT=4

PROBE_SCAN_OS_MSG_TYPE_ID_XMAP = 0x1
PROBE_SCAN_OS_MSG_TYPE_ID_DEPROT = 0x2
PROBE_SCAN_OS_MSG_TYPE_ID_APPLICATION = 0x4
