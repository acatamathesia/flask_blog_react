
# list_to_json : 将list中的所有数据都转换成json对象
def list_to_json(inp_list):
    if type(inp_list) is not list: # 判断list是否是我们需要的类型 -- 使用is判断
        raise Exception("需要list类型，输入类型异常！")
    if len(inp_list) == 0:
        raise Exception('list的长度不能为0')
    if not inp_list[0].__dir__().__contains__('to_dict'):
        raise Exception('元素必须实现了to_dict()方法，并返回一个可用的字典')
    json_list = []
    for item in inp_list:
        json_list.append(item.to_dict())
    return json_list

if __name__ == '__main__':
    list_to_json(())
    print(type([]) is not list)