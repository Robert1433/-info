let editor;

window.onload = function() {
	editor = ace.editor('editor');
	editor.setTheme("ace/theme/monkai");
	editor.session.setMode("ace/mode/c_app");
}

function switchlang(){
	let language = $("#languages").val();
	if(language == 'c' || language == 'cpp')editor.session.setMode("ace/mode/c_cpp");
	else if(language == 'python')editor.session.setMode("ace/mode/python"); else if(language == 'node')editor.session.setMode("ace/mode/javascript"); 
}

function execcodec(){
	$.ajax({
		url:"/static/JS/compile.php",
		method:"POST",
		data:{
			language:$("#languages").val(),
			code:editor.getSession().getValue(),
		},
		success:function(response){
			$(".output").text(response)
		}
	})
}