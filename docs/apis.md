<!--
@Author: lisnb
@Date:   2016-07-27T15:54:14+08:00
@Email:  lisnb.h@hotmail.com
@Last modified by:   lisnb
@Last modified time: 2016-07-27T20:41:04+08:00
-->

- 1. 获取用户信息 params: user_id return: user

- 2. 获取满足条件的用户的所有订单 params: user_id datetime_from datetime_to (skip limit)page complete return: orders

- 3. 获取订单内的商品 params: order_id (skip limit)page commented return: items

- 3.5 获取商品的详细信息 params: item_id return item

- 4. 获取一个商品的所有评价 params: item_id datetime_from datetime_to skip limit level with_picture return: comments

- 5. 提交评价 params: item_id user_id comment_info(dict) return: comment_id

6. 追评 params: item_id user_id original_comment_id comment_info(dict) return: comment_id

- 7. 用户登录 params: user_name user_password return: user

8. 获取待评价商品列表 params: user_id return: items
