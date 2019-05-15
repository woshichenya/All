# -*- coding: UTF-8 -*-
from data_stats.all_table_compute.data_source.db_source.middle_user import DataMiddleUserSource
from data_stats.utils.db_util import insert
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class DataUserProvinceCompute(object):

    province = ('河北省','山西省','辽宁省','吉林省','黑龙江省','江苏省','浙江省','安徽省','福建省','江西省','山东省','河南省','湖北省','湖南省','广东省','海南省','四川省','贵州省','云南省','陕西省','甘肃省','青海省','台湾省','北京市','天津市','上海市','重庆市','内蒙古自治区','广西壮族自治区','宁夏回族自治区','新疆维吾尔自治区','西藏自治区','香港','澳门')

    def __init__(self):
        pass

    def user_province_list(self):
        province_list = DataMiddleUserSource().select_user_province()
        return self._format_province(province_list)

    def _format_province(self,province_list):
        format_province = {}
        for item in province_list:
            if item['province'] == '':
                if '未知' in format_province:
                    format_province['未知'] += item['num']
                else:
                    format_province['未知'] = item['num']
            else:
                for p in self.province:
                    if p.find(item['province']) != -1:
                        if p in format_province:
                            format_province[p] += item['num']
                        else:
                            format_province[p] = item['num']
                        break

        return format_province

