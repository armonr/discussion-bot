from flask import request, render_template, make_response
from discussion_bot import app
from discussion_bot.api_util import create_content, api_url, slack_post
from discussion_bot.bot_util import reply_to


@app.route('/', methods=['GET', 'POST'])
def post():
    post_text = None
    bot_reply = None
    if request.method == 'POST':
        post_text = request.form.get('text')
        bot_reply = reply_to(post_text)
    return render_template('post_form.html', post_text=post_text, bot_reply=bot_reply)


@app.route('/dis_reply', methods=['POST'])
def dis_reply():
    data = request.get_json()
    text = data.get('text')
    site_id = data.get('siteId')
    container_id = data.get('threadId')
    user_id = data.get('userId')
    text = reply_to(text)
    content_data = render_template('post.json', site_id=site_id, container_id=container_id,
                                   user_id=user_id, text=text)
    create_content(api_url(), site_id, 'post', content_data, user_id)
    # post on slack
    slack_post('Wikia id: {siteId}, Post id: {threadId}, Message: {text}'.
               format(text=text, siteId=site_id, threadId=container_id))
    return make_response(('', 200))


@app.route('/reply', methods=['POST'])
def reply(text=None):
    if not text:
        text = request.form.get('text')
    if not text:
        text = request.get_json()['text']
    if not text:
        raise Exception("text was not provided")
    return reply_to(text)

