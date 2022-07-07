
import { init, compileCPPWithInput, compileCPP, compilePythonWithInput, compilePython, fullStat, flush } from 'compilex';
var options = {stats : true};  
init(options);



function compiler(req, res) {
  var code = req.body.code;
  var input = req.body.input;
  var inputRadio = req.body.inputRadio;
  var lang = req.body.lang;
  if (lang === "C" || lang === "C++") {
    if (inputRadio === "true") {
      var envData = { OS: "windows", cmd: "g++", options: { timeout: 10000 } };
      compileCPPWithInput(envData, code, input, function (data) {
        if (data.error) {
          res.send(data.error);
        } else {
          res.send(data.output);	console.log(data.output);
        }
      });
    } else {
      var envData = { OS: "windows", cmd: "g++", options: { timeout: 10000 } };
      compileCPP(envData, code, function (data) {
        res.send(data);
		console.log(data.output);
        //data.error = error message
        //data.output = output value
      });
    }
  }
  if (lang === "Python") {
    if (inputRadio === "true") {
      var envData = { OS: "windows" };
      compilePythonWithInput(envData, code, input, function (data) {
        res.send(data);
      });
    } else {
      var envData = { OS: "windows" };
      compilePython(envData, code, function (data) {
        res.send(data);
      });
    }
  }
};
fullStat(function (data) {
    res.send(data);
  });
flush(function () {
  console.log("All temporary files flushed !");
});