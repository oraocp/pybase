# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# 文件目的：演示如何使用collection包中提供的高级数据结构项
# 创建日期：2018/2/19
# -------------------------------------------------------------------------

def tuple_demo():
    # tuple可迭代，成员类型可不相同，值不可改变
    name_list = ("bob1", "bob2")
    # tuple迭代
    for name in name_list:
        print(name)
    # 在动态语言中可以修改tuple, 改变指针指向的对象
    name_list = ("bob2", "bob3")
    # tuple拆包, 分别赋值
    user_tuple = ("bob", 29, 175)
    name, age, height = user_tuple
    print(name, age, height)
    # 只取name值
    name, *other = user_tuple
    print(name, other)  # bob [29,175] 后续值放在数组中
    # 修改tuple中成员的值
    # 但一般不建议将可变数据对象放在tuple中
    name_tuple = ("bob", [29, 175])
    name_tuple[1].append(22)
    print(name_tuple)
    # 作为dict的key
    user_info_dict = {}
    user_info_dict[name_tuple] = 'type'
    print(user_info_dict)


def main():
    tuple_demo()


if __name__ == '__main__':
    main()
