"""
	Auth:xiaoran 
	Date:2015/10
"""

"""
     algor_search_img is search name in name_list 
     return like [(level,match),(),....]
     match is from name_list which like name
     level is how much name like name_list
     attr is name_list attraubite 
 Note:
     level : from 1 -> 5
     5: complate like
     4: name complate in match
     3: match complate in name
     2: head 3 world is like match
     1: head 1 world  is like match
"""
def algor_search_img(name,obj_list,attr=None):
    match_list = list()
    result_list = list()
    if not obj_list or not name:
        return result_list
    if attr:
        for obj in obj_list:
            obj_name = getattr(obj,attr,None) 
            if obj_name:
                if obj_name == name:
                    result_list.append((5,obj))
                elif obj_name.startswith(name) or obj_name.endswith(name):
                    result_list.append((4,obj))
                elif name.startswith(obj_name) or name.endswith(obj_name):
                    result_list.append((3,obj))
                elif name[:3] == obj_name[:3]:
                    result_list.append((2,obj))
                elif name[0] == obj_name[0]:
                    result_list.append((1,obj)) 
    else:
        match_list = obj_list
        if name in match_list:
            result_list.append((5,name))
        for match in match_list:
            if match.startswith(name) or match.endswith(name):
                result_list.append((4,match))
            elif name.startswith(match) or name.endswith(match):
                result_list.append((3,match))
            elif match.startswith(name[:3]):
                result_list.append((2,match))
            elif match[0] == name[0]:
                result_list.append((1,match))
    result_list.sort(reverse=True)
    return result_list
