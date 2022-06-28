function showPreview(){
  let htmlCode = document.getElementById("htmlCode").value;
  let cssCode = "<style>" + document.getElementById("cssCode").value + "</style>";
  let jsCode = "<scri" + "pt" + document.getElementById("jsCode").value + "</scri" + "pt";
  var frame = document.getElementById("preview-window").contentWindow.document;
  frame.open();
  frame.write(htmlCode + cssCode + jsCode)
  frame.close();
}