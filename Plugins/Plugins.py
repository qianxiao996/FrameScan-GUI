#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: cms漏洞库
referer: unknow
author: qianxiao996
'''
#.idea

#acsoft
from Plugins.acsoft.GetFileContent_fileread import GetFileContent_fileread
from Plugins.acsoft.GetFile_fileread import GetFile_fileread
from Plugins.acsoft.GetXMLList_fileread import GetXMLList_fileread

#autoset
from Plugins.autoset.phpmyadmin_unauth import phpmyadmin_unauth

#bash
from Plugins.bash.shellshock import BaseVerify

#cmseasy
from Plugins.cmseasy.header_detail_sqli import header_detail_sqli

#couchdb
from Plugins.couchdb.unauth import unauth_BaseVerify

#dedecms
from Plugins.dedecms.download_redirect import download_redirect
from Plugins.dedecms.error_trace_disclosure import error_trace_disclosure
from Plugins.dedecms.recommend_sqli import recommend_sqli
from Plugins.dedecms.search_typeArr_sqli import search_typeArr_sqli
from Plugins.dedecms.version import version

#discuz
from Plugins.discuz.focus_flashxss import focus_flashxss
from Plugins.discuz.forum_message_ssrf import forum_message_ssrf
from Plugins.discuz.plugin_ques_sqli import plugin_ques_sqli
from Plugins.discuz.x25_path_disclosure import x25_path_disclosure

#diyou
from Plugins.diyou.latesindex_sqli import latesindex_sqli
from Plugins.diyou.url_fileread import url_fileread

#dorado
from Plugins.dorado.default_passwd import default_passwd_BaseVerify

#dreamgallery
from Plugins.dreamgallery.album_id_sqli import album_id_sqli

#dswjcms
from Plugins.dswjcms.p2p_multi_sqli import p2p_multi_sqli

#ecscms
from Plugins.ecscms.MoreIndex_sqli import MoreIndex_sqli

#ecshop
from Plugins.ecshop.eshop_all_code_exec import all_code_exec
from Plugins.ecshop.orderid_sqli import flow_orderid_sqli
from Plugins.ecshop.uc_code_sqli import uc_code_sqli

#esccms
from Plugins.esccms.selectunitmember_unauth import selectunitmember_unauth

#etmdcp
from Plugins.etmdcp.Load_filedownload import Load_filedownload

#eyou
from Plugins.eyou.admin_id_sqli import admin_id_sqli
from Plugins.eyou.resetpw import resetpw
from Plugins.eyou.user_kw_sqli import user_kw_sqli
from Plugins.eyou.weakpass import weakpass

#fastmeeting
from Plugins.fastmeeting.download_filedownload import download_filedownload

#finecms
from Plugins.finecms.uploadfile import uploadfile
from Plugins.finecms.v508_getshell import v508_getshell
from Plugins.finecms.v508_write_file import v508_write_file

#foosun
from Plugins.foosun.City_ajax_sqli import City_ajax_sqli

#fsmcms
from Plugins.fsmcms.columninfo_sqli import columninfo_sqli
from Plugins.fsmcms.p_replydetail_sqli import p_replydetail_sqli
from Plugins.fsmcms.setup_reinstall import setup_reinstall

#glassfish
from Plugins.glassfish.fileread import fileread_BaseVerify

#goahead
from Plugins.goahead.LD_PRELOAD_rce import LD_PRELOAD_rce_BaseVerify

#gobetters
from Plugins.gobetters.multi_sqli import multi_sqli

#gowinsoft_jw
from Plugins.gowinsoft_jw.jw_multi_sqli import jw_multi_sqli

#gpower
from Plugins.gpower.users_disclosure import users_disclosure

#hanweb
from Plugins.hanweb.downfile_filedownload import downfile_filedownload
from Plugins.hanweb.readxml_fileread import readxml_fileread
from Plugins.hanweb.VerifyCodeServlet_install import VerifyCodeServlet_install

#hfs
from Plugins.hfs.rejetto_search_rce import rejetto_search_rce_BaseVerify

#Hishop
from Plugins.Hishop.productlist_sqli import productlist_sqli

#hudson
from Plugins.hudson.ws_disclosure import ws_disclosure_BaseVerify

#iGenus
from Plugins.iGenus.code_exec import code_exec
from Plugins.iGenus.login_Lang_fileread import login_Lang_fileread
from Plugins.iGenus.syslogin_Lang_fileread import syslogin_Lang_fileread

#iis
from Plugins.iis.ms15034_httpsys_rce import ms15034_httpsys_rce_BaseVerify
from Plugins.iis.webdav_rce import webdav_rce_BaseVerify

#inspur
from Plugins.inspur.ecgap_displayNewsPic_sqli import ecgap_displayNewsPic_sqli
from Plugins.inspur.multi_sqli import multi_sqli

#intel
from Plugins.intel.amt_crypt_bypass import amt_crypt_bypass_BaseVerify

#iwms
from Plugins.iwms.bypass_js_delete import bypass_js_delete

#jeecg
from Plugins.jeecg.pwd_reset import pwd_reset

#jeecms
from Plugins.jeecms.fpath_filedownload import fpath_filedownload

#joomla
from Plugins.joomla.com_docman_lfi import com_docman_lfi
from Plugins.joomla.index_list_sqli import index_list_sqli

#jumboecms
from Plugins.jumboecms.slide_id_sqli import slide_id_sqli

#kingdee
from Plugins.kingdee.conf_disclosure import conf_disclosure
from Plugins.kingdee.filedownload import filedownload
from Plugins.kingdee.logoImgServlet_fileread import logoImgServlet_fileread
from Plugins.kingdee.resin_dir_path_disclosure import resin_dir_path_disclosure

#kxmail
from Plugins.kxmail.login_server_sqli import login_server_sqli

#lbcms
from Plugins.lbcms.webwsfw_bssh_sqli import webwsfw_bssh_sqli

#libsys
from Plugins.libsys.ajax_asyn_link_fileread import ajax_asyn_link_fileread
from Plugins.libsys.ajax_asyn_link_old_fileread import ajax_asyn_link_old_fileread
from Plugins.libsys.ajax_get_file_fileread import ajax_get_file_fileread

#live800
from Plugins.live800.downlog_filedownload import downlog_filedownload
from Plugins.live800.fileDownloadServer_fileread import fileDownloadServer_fileread
from Plugins.live800.loginAction_sqli import loginAction_sqli
from Plugins.live800.sta_export_sqli import sta_export_sqli

#looyu
from Plugins.looyu.down_filedownload import down_filedownload

#metinfo
from Plugins.metinfo.getpassword_sqli import getpassword_sqli
from Plugins.metinfo.login_check_sqli import login_check_sqli

#ndstar
from Plugins.ndstar.six_sqli import six_sqli

#nitc
from Plugins.nitc.index_language_id_sqli import index_language_id_sqli
from Plugins.nitc.suggestwordList_sqli import suggestwordList_sqli

#opensns
from Plugins.opensns.index_arearank import index_arearank
from Plugins.opensns.index_getshell import index_getshell

#others
from Plugins.others.alkawebs_viewnews_sqli import alkawebs_viewnews_sqli
from Plugins.others.anmai_grghjl_stuNo_sqli import anmai_grghjl_stuNo_sqli
from Plugins.others.anmai_teachingtechnology_sqli import anmai_teachingtechnology_sqli
from Plugins.others.caitong_multi_sleep_sqli import caitong_multi_sleep_sqli
from Plugins.others.caitong_multi_sqli import caitong_multi_sqli
from Plugins.others.clib_kindaction_fileread import clib_kindaction_fileread
from Plugins.others.clib_kinweblistaction_download import clib_kinweblistaction_download
from Plugins.others.damall_selloffer_sqli import damall_selloffer_sqli
from Plugins.others.dkcms_database_disclosure import dkcms_database_disclosure
from Plugins.others.domino_unauth import domino_unauth
from Plugins.others.efuture_downloadAct_filedownload import efuture_downloadAct_filedownload
from Plugins.others.eis_menu_left_edit_sqli import eis_menu_left_edit_sqli
from Plugins.others.euse_study_multi_sqli import euse_study_multi_sqli
from Plugins.others.forease_fileinclude_code_exec import forease_fileinclude_code_exec_BaseVerify
from Plugins.others.gevercms_downLoadFile_filedownload import gevercms_downLoadFile_filedownload
from Plugins.others.gn_consulting_sqli import gn_consulting_sqli
from Plugins.others.gpcsoft_ewebeditor_weak import gpcsoft_ewebeditor_weak
from Plugins.others.gxwssb_fileDownloadmodel_download import gxwssb_fileDownloadmodel_download
from Plugins.others.haohan_FileDown_filedownload import haohan_FileDown_filedownload
from Plugins.others.hezhong_list_id_sqli import hezhong_list_id_sqli
from Plugins.others.hjsoft_sqli import hjsoft_sqli
from Plugins.others.hnkj_researchinfo_dan_sqli import hnkj_researchinfo_dan_sqli
from Plugins.others.hongan_dlp_struts_exec import hongan_dlp_struts_exec
from Plugins.others.huaficms_bypass_js import huaficms_bypass_js
from Plugins.others.ips_community_suite_code_exec import ips_community_suite_code_exec
from Plugins.others.jiuyu_library_struts_exec import jiuyu_library_struts_exec
from Plugins.others.jxt1039_unauth import jxt1039_unauth
from Plugins.others.kj65n_monitor_sqli import kj65n_monitor_sqli
from Plugins.others.lianbang_multi_bypass_priv import lianbang_multi_bypass_priv
from Plugins.others.mainone_b2b_Default_sqli import mainone_b2b_Default_sqli
from Plugins.others.mainone_ProductList_sqli import mainone_ProductList_sqli
from Plugins.others.mainone_SupplyList_sqli import mainone_SupplyList_sqli
from Plugins.others.mallbuilder_change_status_sqli import mallbuilder_change_status_sqli
from Plugins.others.mingteng_cookie_deception import mingteng_cookie_deception
from Plugins.others.newedos_multi_sqli import newedos_multi_sqli
from Plugins.others.nongyou_Item2_sqli import nongyou_Item2_sqli
from Plugins.others.nongyou_multi_sqli import nongyou_multi_sqli
from Plugins.others.nongyou_ShowLand_sqli import nongyou_ShowLand_sqli
from Plugins.others.nongyou_sleep_sqli import nongyou_sleep_sqli
from Plugins.others.rap_interface_struts_exec import rap_interface_struts_exec
from Plugins.others.shiyou_list_keyWords_sqli import shiyou_list_keyWords_sqli
from Plugins.others.sinda_downloadfile_download import sinda_downloadfile_download
from Plugins.others.skytech_bypass_priv import skytech_bypass_priv
from Plugins.others.skytech_geren_list_page_sqli import skytech_geren_list_page_sqli
from Plugins.others.star_PostSuggestion_sqli import star_PostSuggestion_sqli
from Plugins.others.suntown_upfile_fileupload import suntown_upfile_fileupload
from Plugins.others.tianbo_Class_Info_sqli import tianbo_Class_Info_sqli
from Plugins.others.tianbo_St_Info_sqli import tianbo_St_Info_sqli
from Plugins.others.tianbo_TCH_list_sqli import tianbo_TCH_list_sqli
from Plugins.others.tianbo_Type_List_sqli import tianbo_Type_List_sqli
from Plugins.others.tpshop_eval_stdin_code_exec import tpshop_eval_stdin_code_exec
from Plugins.others.workyi_multi_sqli import workyi_multi_sqli
from Plugins.others.xtcms_download_filedownload import xtcms_download_filedownload
from Plugins.others.xuezi_ceping_unauth import xuezi_ceping_unauth
from Plugins.others.yaojie_steel_struts_exec import yaojie_steel_struts_exec
from Plugins.others.yeu_disclosure_uid import yeu_disclosure_uid
from Plugins.others.zfcgxt_UserSecurityController_getpass import zfcgxt_UserSecurityController_getpass
from Plugins.others.zf_cms_FileDownload import zf_cms_FileDownload
from Plugins.others.zhuofan_downLoadFile_download import zhuofan_downLoadFile_download

#pageadmin
from Plugins.pageadmin.forge_viewstate import forge_viewstate

#php
from Plugins.php.expose_disclosure import expose_disclosure_BaseVerify
from Plugins.php.fastcgi_read import fastcgi_read_BaseVerify

#php168
from Plugins.php168.login_getshell import login_getshell

#phpcms
from Plugins.phpcms.authkey_disclosure import authkey_disclosure
from Plugins.phpcms.digg_add_sqli import digg_add_sqli
from Plugins.phpcms.flash_upload_sqli import flash_upload_sqli
from Plugins.phpcms.product_code_exec import product_code_exec
from Plugins.phpcms.v961_fileread import v961_fileread
from Plugins.phpcms.v96_sqli import v96_sqli
from Plugins.phpcms.v9_flash_xss import v9_flash_xss

#phpmyadmin
from Plugins.phpmyadmin.setup_lfi import setup_lfi

#phpok
from Plugins.phpok.api_param_sqli import api_param_sqli
from Plugins.phpok.remote_image_getshell import remote_image_getshell
from Plugins.phpok.res_action_control_filedownload import res_action_control_filedownload

#phpstudy
from Plugins.phpstudy.phpmyadmin_defaultpwd import phpmyadmin_defaultpwd
from Plugins.phpstudy.phpstudy_backdoor import phpstudy_backdoor
from Plugins.phpstudy.probe import probe

#piaoyou
from Plugins.piaoyou.int_order_sqli import int_order_sqli
from Plugins.piaoyou.multi_sqli import multi_sqli
from Plugins.piaoyou.newsview_list import newsview_list
from Plugins.piaoyou.six2_sqli import six2_sqli
from Plugins.piaoyou.six_sqli import six_sqli
from Plugins.piaoyou.ten_sqli import ten_sqli

#PKPMBS
from Plugins.PKPMBS.addresslist_keyword_sqli import addresslist_keyword_sqli
from Plugins.PKPMBS.guestbook_sqli import guestbook_sqli
from Plugins.PKPMBS.MsgList_sqli import MsgList_sqli

#Plugins.py

#pstar
from Plugins.pstar.isfLclInfo_sqli import isfLclInfo_sqli
from Plugins.pstar.qcustoms_sqli import qcustoms_sqli
from Plugins.pstar.warehouse_msg_01_sqli import warehouse_msg_01_sqli

#qibocms
from Plugins.qibocms.js_f_id_sqli import js_f_id_sqli
from Plugins.qibocms.search_code_exec import search_code_exec
from Plugins.qibocms.search_sqli import search_sqli
from Plugins.qibocms.s_fids_sqli import s_fids_sqli

#resin
from Plugins.resin.viewfile_fileread import resin_viewfile_fileread_BaseVerify

#ruvar
from Plugins.ruvar.multi_sqli import multi_sqli
from Plugins.ruvar.multi_sqli2 import multi_sqli2
from Plugins.ruvar.multi_sqli3 import multi_sqli3

#sangfor
from Plugins.sangfor.ad_script_command_exec import ad_script_command_exec_BaseVerify

#seacms
from Plugins.seacms.order_code_exec import order_code_exec
from Plugins.seacms.search_code_exec import search_code_exec
from Plugins.seacms.search_jq_code_exec import search_jq_code_exec
from Plugins.seacms.v655_code_exec import v655_code_exec

#shadowsit
from Plugins.shadowsit.selector_lfi import selector_lfi

#shop360
from Plugins.shop360.do_filedownload import do_filedownload

#shop7z
from Plugins.shop7z.order_checknoprint_sqli import order_checknoprint_sqli

#shopex
from Plugins.shopex.phpinfo_disclosure import phpinfo_disclosure

#shopnc
from Plugins.shopnc.index_class_id_sqli import index_class_id_sqli

#shopnum
from Plugins.shopnum.GuidBuyList_sqli import GuidBuyList_sqli
from Plugins.shopnum.ProductDetail_sqli import ProductDetail_sqli
from Plugins.shopnum.ProductListCategory_sqli import ProductListCategory_sqli
from Plugins.shopnum.ShoppingCart1_sqli import ShoppingCart1_sqli

#siteengine
from Plugins.siteengine.comments_module_sqli import comments_module_sqli

#siteserver
from Plugins.siteserver.background_administrator_sqli import background_administrator_sqli
from Plugins.siteserver.background_keywordsFilting_sqli import background_keywordsFilting_sqli
from Plugins.siteserver.background_log_sqli import background_log_sqli
from Plugins.siteserver.background_taskLog_sqli import background_taskLog_sqli
from Plugins.siteserver.UserNameCollection_sqli import UserNameCollection_sqli

#smartoa
from Plugins.smartoa.multi_filedownload import multi_filedownload

#smtp
from Plugins.smtp.starttls_plaintext_inj import starttls_plaintext_inj_BaseVerify

#speedcms
from Plugins.speedcms.list_cid_sqli import list_cid_sqli

#srun
from Plugins.srun.download_file_filedownload import download_file_filedownload_BaseVerify
from Plugins.srun.index_file_filedownload import index_file_filedownload_BaseVerify
from Plugins.srun.rad_online_bypass_rce import rad_online_bypass_rce_BaseVerify
from Plugins.srun.rad_online_username_rce import rad_online_username_rce_BaseVerify
from Plugins.srun.user_info_uid_rce import user_info_uid_rce_BaseVerify

#tcexam
from Plugins.tcexam.reinstall_getshell import reinstall_getshell

#thinkphp
from Plugins.thinkphp.code_exec import code_exec
from Plugins.thinkphp.onethink_category_sqli import onethink_category_sqli
from Plugins.thinkphp.v5x_code_exec import v5x_code_exec_1

#thinksns
from Plugins.thinksns.category_code_exec import category_code_exec

#tomcat
from Plugins.tomcat.put_exec import put_exec_BaseVerify

#topsec
from Plugins.topsec.change_lan_filedownload import change_lan_filedownload_BaseVerify

#trs
from Plugins.trs.ids_auth_disclosure import ids_auth_disclosure
from Plugins.trs.infogate_register import infogate_register
from Plugins.trs.infogate_xxe import infogate_xxe
from Plugins.trs.inforadar_disclosure import inforadar_disclosure
from Plugins.trs.lunwen_papercon_sqli import lunwen_papercon_sqli
from Plugins.trs.was40_passwd_disclosure import was40_passwd_disclosure
from Plugins.trs.was40_tree_disclosure import was40_tree_disclosure
from Plugins.trs.was5_config_disclosure import was5_config_disclosure
from Plugins.trs.was5_download_templet import was5_download_templet
from Plugins.trs.wcm_default_user import wcm_default_user
from Plugins.trs.wcm_infoview_disclosure import wcm_infoview_disclosure
