    function output_templates(){
      let getform= document.forms[0]
      //console.log(getform.elements[0].value==0);
      getform.elements[0].value==0 ? console.log("入力項目が足りません"):make_templates(getform);
    }

    function make_templates(args){
      console.log(args.elements[0].value);
      console.log(args.elements[1].value);
      console.log(simplemde.value());
      make_templates_py(args);
    }
async function make_templates_py(args){
        let logs= eel.outputTemplates(args.elements[0].value,args.elements[1].value,simplemde.value());
        //console.log(await eel.outputTemplates(args.elements[0].value,args.elements[1].value));
        args.elements[0].value="";
      }
