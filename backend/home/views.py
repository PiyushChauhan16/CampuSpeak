from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from home.models import post, user, comment, userSetting
from home.sentimentAnalysis import load_models, predict
# Create your views here.
def login (request):
    print ("in login")
    print (request, request.POST.get ("postContent"))
    request.session["uid"] = '8f7033cff4ae41358ff93675530dc8d7'
    return redirect ("index")

def index(request):
    # print (args[0])

    vectoriser, LRmodel = load_models()
    print ("models loaded")
    # Text to classify should be in a list.
    text = ["I hate twitter",
            "May the Force be with you.",
            "Mr. Stark, I don't feel so good",
            "Today was a great day for me. I got placed at TRC",
            "i just hate baigan"
            ]
    
    df = predict(vectoriser, LRmodel, text)
    print(df.head())


    uuid_string = request.session.get('uid', None)
    userTuple = get_object_or_404(user, uid=uuid_string)
    isEnable = userSetting.objects.all ().filter (uid = uuid_string)[0].isEnable

    print (uuid_string)
    print ("in index")
    print (request, request.POST.get ("postContent"))

    if request.method == "GET" and request.GET.get ("isEnable") != None:
        print (request.GET.get ("isEnable"))
        updatedIsEnable = request.GET.get ("isEnable")
        userSettingTuple = userSetting.objects.all ().filter (uid = uuid_string)[0]
        userSettingTuple.isEnable = updatedIsEnable
        isEnable = updatedIsEnable
        userSettingTuple.save ()

    elif request.method == "POST":
        postContent = request.POST.get ("postContent")
        newPost = post (postContent = postContent, uid= userTuple)
        newPost.save ()

    recentPost = []
    for item in post.objects.all ():
        print (type(item.uid), type(item.uid.uid))

        userOfPost = user.objects.all ().filter (uid = item.uid.uid)[0]
        df = predict(vectoriser, LRmodel, [item.postContent])

        
  

        dfToList= (str (df.head ()).split ())
        categorizeContent = dfToList[len (dfToList)-1]

        
        # print ("category:",categorizeContent.head (), type(str(categorizeContent.head())))
        print (userOfPost, userOfPost.branch, userOfPost.batch)
        dataUsed = {
            "pid":item.pid,
            "postContent": item.postContent,
            "branch": userOfPost.branch,
            "batch": userOfPost.batch,
            "categorizeContent": categorizeContent
        }
        recentPost.insert (0,dataUsed)
    
    print (isEnable, type(isEnable))
    
    return render (request, "index.html", {"data":recentPost, 
                                           "authPin": userTuple.authPin, 
                                           "uid":uuid_string,
                                           "isEnable": isEnable})


def fullPost (request, *args, **kwargs):
    print ("request:", request.GET.get ("pid"))
    postId = request.GET.get ("pid")
    postIdTuple = post.objects.all ().filter (pid = postId)[0]
    userId = request.GET.get ("uid")
    userIdTuple = user.objects.all ().filter (uid = userId)[0]
    userBatch = request.GET.get ("batch")
    userBranch = request.GET.get ("branch")
    

    print ("commentContent:", request.GET.get ("commentContent"))
    if request.GET.get ("commentContent") != None:
        commentContent = request.GET.get ("commentContent")
        commentObj = comment (uid = userIdTuple, pid = postIdTuple, commentContent = commentContent, replyId = postId)
        commentObj.save ()
    print ("userTuple:", userIdTuple)
    print ("postTuple:",postIdTuple)

    allComments= comment.objects.filter (pid = postId).filter (replyId = postId)
    commentData = []

    for item in allComments:
        commentUserId = item.uid.uid
        # print ("item.pid:",item.uid.uid)
        commentUser = user.objects.all ().filter (uid = commentUserId)[0]

        tempdata = {
            "cid":item.cid,
            "commentContent": item.commentContent,
            "batch": commentUser.batch,
            "branch": commentUser.branch
        }

        commentData.insert (0, tempdata)


        
    data = {
        "pid": postIdTuple.pid,
        "postContent": postIdTuple.postContent,
        "uid": userId,
        "commentData": commentData,
        "batch":userBatch,
        "branch": userBranch
    }
    allComments = comment.objects.filter (pid = postId).filter (replyId = postId)

    print (allComments)
    return render (request, "fullPost.html", data)


def commentReply (request):
    userId = request.GET.get ("uid")
    postId = request.GET.get ("pid")
    commentId = request.GET.get ("cid")
    userTuple = user.objects.all ().filter (uid = userId)[0]
    postTuple = post.objects.all ().filter (pid = postId)[0]
    commentTuple = comment.objects.all ().filter (cid = commentId)[0]

    if request.GET.get ("replyContent") != None:
        replyContent = request.GET.get ("replyContent")
        commentObj = comment (uid = userTuple, pid = postTuple, commentContent = replyContent, replyId = commentId)
        commentObj.save ()
    #print (type(userTuple), postTuple, commentTuple)

    allComments= comment.objects.filter (pid = postId).filter (replyId = commentId)
    replyData = []

    for item in allComments:
        commentUserId = item.uid.uid
        # print ("item.pid:",item.uid.uid)
        commentUser = user.objects.all ().filter (uid = commentUserId)[0]

        tempdata = {
            "commentReplyId":item.cid,
            "replyContent": item.commentContent,
            "batch": commentUser.batch,
            "branch": commentUser.branch
        }

        replyData.insert (0, tempdata)

    data = {
        "uid":userId,
        "pid":postId,
        "cid":commentId,
        "commentContent" : commentTuple.commentContent,
        "replyData": replyData
    }
    
    print (commentTuple.commentContent)
    return render (request,"commentReply.html", data)