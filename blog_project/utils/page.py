
class Page:
    page_size = 15

    @classmethod
    def auto_page(cls, old_list, page_num):
        page_num = int(page_num)
        start_index = (page_num-1)*cls.page_size
        end_index = (start_index+cls.page_size)
        if end_index > len(old_list):
            end_index = len(old_list)
        try:
            sub_list = old_list[start_index:end_index]
        except BaseException as e:
            print(e)
            sub_list = old_list[0:end_index]
        return sub_list


# 测试分页函数好不好用
if __name__ == "__main__":
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    print(Page.auto_page(list,2))