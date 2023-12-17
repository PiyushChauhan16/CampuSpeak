const postContentBtnRef = document.querySelector (".post-content");
const sideBarRef = document.querySelector (".sidebar");
const validPin = JSON.parse('{{ authPin|safe }}');
let isSecure = '{{isEnable}}';
const authPinBtnRef = document.querySelector (".auth-pin-btn");


if (isSecure === 1 || isSecure === "1") authPinBtnRef.innerHTML = "SECURE"
else authPinBtnRef.innerHTML = "INSECURE"
console.log (isSecure);

authPinBtnRef.addEventListener ("click", ()=>{
    if (isSecure === 1 || isSecure === "1"){
        console.log ("making it insecure")
        authPinBtnRef.innerHTML = "INSECURE";
        
        window.location.href = '{%url "index" %}?isEnable=0'

    }
    else{
        console.log ("making it secure")
        authPinBtnRef.innerHTML = "SECURE";
        window.location.href = '{%url "index" %}?isEnable=1'
        
    }
})



postContentBtnRef.addEventListener ("click", ()=>{

    console.log (sideBarRef.children)
    childrenLength = sideBarRef.children.length;

    if (childrenLength == 1){
        var createPost = document.createElement ("div");
        createPost.className = "create-post"
        createPost.innerHTML = 
        `
        <button class = "cancel-btn">CANCEL</button>
        <form action="/index/" method="POST" class = "form-div">
        {% csrf_token %}
        <label for="postContent"> Write your post</label>
        <textarea name="postContent" id="post" style="height: 100px;"></textarea>
        <input type="text" class = "auth-input" />
        <div class = "msg"></div>
        <button class="post-btn">Post</button>
        </form>`
        sideBarRef.appendChild (createPost);

        
        const authInputRef = document.querySelector (".auth-input");
        const postBtnRef = document.querySelector (".post-btn");
        const cancelBtnRef = document.querySelector (".cancel-btn")
        const createPostRef = document.querySelector (".create-post")

        cancelBtnRef.addEventListener ("click", ()=>{
            sideBarRef.removeChild (createPostRef)
        })

        if (isSecure === 0 || isSecure === "0"){
            authInputRef.classList.add ("hidden");
            postBtnRef.disabled = false;
            document.querySelector (".msg").innerHTML = "";
            authInputRef.value = "";
        }
        else{
            authInputRef.classList.remove ("hidden")
            postBtnRef.disabled = true;
        }

        
        authInputRef.addEventListener ("input", (e)=>{
            console.log (typeof e.target.value,typeof validPin);
            console.log (e.target.value === validPin);

            if (Number(e.target.value) !== (validPin)){
                document.querySelector (".msg").innerHTML = "Incorrect Password";
                postBtnRef.disabled = true;
            }
            else {
                document.querySelector (".msg").innerHTML = "Correct Password";
                postBtnRef.disabled = false;
            }
            
        });
    }
    
})








//fullPost
commentBoxRef = document.querySelector ("#comment-box");
addCommentBtnRef = document.querySelector (".add-comment-btn");
commentContent = "";

commentBoxRef.addEventListener ("input", (e)=>{
    commentContent = e.target.value;
})


addCommentBtnRef.addEventListener ("click", ()=>{
    console.log (commentContent)
    console.log ("click");
    window.location.href = `{% url "fullPost" %}?pid={{pid}}&uid={{uid}}&commentContent=${commentContent}`
})





console.log ("onokjdhf")