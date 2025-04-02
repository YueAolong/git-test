# from flask import Flask
# app = Flask(__name__)
#
#
# @app.route('/')  # 定义路由：当访问根路径时触发
# def home():
#     return "李凌萱"
#
#
# @app.route('/about')
# def about_page():
#     return '这是关于页面'
#
#
# @app.route('/user/<username>')
# def show_user(username):
#     return f'用户：{username}'
#
#
# if __name__ == '__main__':
#     # app.run(debug=True)  # 启动服务器
#     app.run(host='0.0.0.0', port=5000, debug=True)
# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route('/blog')
# def blog():
#     # 渲染模板并传递数据
#     return render_template('index.html',
#                            title='我的博客',
#                            content='第一篇博客文章')
#
# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         # 获取表单数据
#         username = request.form['username']
#         return f"欢迎 {username}!"  # 返回欢迎信息
#     return render_template('login.html')  # GET请求时渲染登录表单
#
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# 模拟数据库（可以后续替换为实际的数据库）
posts = [
    {'id': 1, 'title': '第一篇文章', 'content': '这是我的第一篇博客'},
    {'id': 2, 'title': '学习Flask', 'content': '今天学习了Web开发'}
]

# 首页，显示所有文章
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# 文章详情页
@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    return render_template('post.html', post=post)

# 创建文章页面
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        new_post = {
            'id': len(posts) + 1,
            'title': request.form['title'],
            'content': request.form['content']
        }
        posts.append(new_post)  # 将新文章添加到数据库（即模拟数据库列表）
        return redirect('/')  # 提交后重定向到首页
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)

