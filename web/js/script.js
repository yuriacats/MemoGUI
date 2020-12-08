    function output_templates(){
      let getform= document.forms[0];
      //console.log(getform.elements[0].value==0);
      getform.elements[0].value == 0 ? console.log("入力項目が足りません"):make_templates(getform);
    }

    function make_templates(args){
      //console.log(args.elements[0].value);
      //console.log(args.elements[1].value);
      //console.log(simplemde.value());
      make_templates_py(args);
    }
    async function make_templates_py(args){
        let logs= eel.outputTemplates(args.elements[0].value,args.elements[1].value,simplemde.value());
        //console.log(await eel.outputTemplates(args.elements[0].value,args.elements[1].value));
        args.elements[0].value="";
      }

    function meke_memo(){
        let getform=document.forms[1];
        make_memo_py(getform);
      }
    async function make_memo_py(args){
    let logs= await eel.input_memos(args.elements[0].value,args.elements[1].value )();
    output_memos()
    args.elements[0].value="";
    args.elements[1].value="";
    return 0;
    }
    function output_memos(){
        pull_memos().then(memos=>{for(i=0;i<memos.length;i++){white_memo(memos[i][0],memos[i][1]);}});
    }
    async function pull_memos(){
        //メモを呼び出す
        return await eel.memo_reload()();
    }
    function white_memo(title,text){
    if ('content' in document.createElement('template')) {
     let tbody = document.querySelector('#memo_container');
     let template = document.querySelector('#memo_template');
     let clone = template.content.cloneNode(true);
     let p = clone.querySelectorAll("p");
     p[0].textContent=title;
     p[1].textContent=text;
     tbody.appendChild(clone);
    }
    }