const htmleditor = CodeMirror(document.querySelector(".editor .code .html-code"),{lineNumbers:true,tabSize:4,mode:"xml"});
const csseditor = CodeMirror(document.querySelector(".editor .code .css-code"),{lineNumbers:true,tabSize:4,mode:"css"});
const jseditor = CodeMirror(document.querySelector(".editor .code .js-code"),{lineNumbers:true,tabSize:4,mode:"javascript"});

document.querySelector("#run-btn").addEventListener("click",function() {
  let htmlcode = htmleditor.getValue();
  let csscode = "<style>" + csseditor.getValue() + "/style";
  let jscode = "<scri" + "pt>" + jseditor.getValue() + "</scri" + "pt>";
  let previewWindow = document.querySelector("#preview-window").contentWindow.document;
  previewWindow.open();previewWindow.write(htmlcode + csscode + jscode);
  previewWindow.close();
});