import sys

replies_def = 'replies = [{replies}]\n'
count_def = 'count = {count}\n'

body = '''
var i = 0

function post(reply) {
var replyData = {
    tid: ajaxify.data.tid,
    handle: undefined,
    content: reply
    }
socket.emit('posts.reply', replyData, function(err, data) {
        if (err) {
            return err
        }
        if (data && data.queued) {
            return nil
        }
    })
}

setInterval(function() {
        if (i >= count) {
            return
        }
        console.log('Posting reply ' + i)
        err = post(replies[i])
        if (err) {
            console.log('Post reply ' + i + ' failed')
        } else {
            console.log('Post reply ' + i + ' success')
            i++
        }
    }, 11000)
'''

f = open(sys.argv[1])
line = f.readline()
replies = []
reply = '`'
while line:
    reply = reply + line.replace('`', '\\`')
    if line == '\n' and reply != '`\n':
        reply = reply + '`'
        replies.append(reply)
        reply = '`'
    line = f.readline()
f.close()

replies_str = replies_def.format(replies=', '.join(replies))
count_str = count_def.format(count=len(replies))
print(replies_str)
print(count_str)

f = open(sys.argv[2], 'w')
f.write(replies_str + count_str + body)
f.close()
