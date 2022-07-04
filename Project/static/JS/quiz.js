
document.addEventListener('DOMContentLoaded', () => {
    const timeLeftDisplay = document.querySelector('#time-left');
    const startbtn = document.querySelector('.start-button');
    let timeLeft = {{ quiz.time }
};
 
    function countDown() {
        setInterval(function () {
            if (timeLeft <= 0) {
                clearInterval(timeLeft = 0)
            }
            if (timeLeft == 0) {
                $(".ans").attr("disabled", true);
            }
            timeLeftDisplay.innerHTML = timeLeft
            timeLeft--;
        }, 1000)
    }
    startbtn.addEventListener('click', countDown)
    });


	const url = window.location.href
   const quizBox = document.getElementById('quiz-box')
   const resultBox = document.getElementById('result-box')
   const totalScore = document.getElementById('total')
   $.ajax({
       type: 'GET',
       url: `${url}data`,
       success: function (response) {
           const data = response.data
           data.forEach(ele => {
               for (const [question, answers] of Object.entries(ele)) {
                   quizBox.innerHTML += `
                   <hr class="ques" style="display:none">
                   <div class="mb-2 ques" style="display:none">
                       <b>${question}</b>
                   </div>
               `
                   $('.start-button').click(function () {
                       $(".ques").show();
                   });
                   answers.forEach(answer => {
                       quizBox.innerHTML += `
                       <div>
                           <input type="radio" class="ans" style="display:none" id="${question}-${answer}" name="${question}" value="${answer}">
                           <label for="${question}" style="display:none" class="answer">${answer}</label>
                       </div>
                   `

				   marks.forEach(res=>{
					const resDiv = document.createElement("div")
					for (const [question, resp] of Object.entries(res)){
						resDiv.innerHTML += question
						const cls = ['container', 'p-3', 'text-light', 'h6']
						resDiv.classList.add(...cls)
						if (resp=='not answered') {
							resDiv.innerHTML += '- not answered'
							resDiv.classList.add('bg-info')
						}
						else {
							const answer = resp['answered']
							const correct = resp['correct_answer']
							if (answer == correct) {
								resDiv.classList.add('bg-success')
								resDiv.innerHTML += ` answered: ${answer}`
							} else {
								resDiv.classList.add('bg-danger')
								resDiv.innerHTML += ` | correct answer: ${correct}`
								resDiv.innerHTML += ` | answered: ${answer}`
							}
						}
					}
					resultBox.append(resDiv)
				})
			},if (answer == correct) {
				resDiv.classList.add('bg-success')
				resDiv.innerHTML += ` answered: ${answer}`
			} else {
				resDiv.classList.add('bg-danger')
				resDiv.innerHTML += ` | correct answer: ${correct}`
				resDiv.innerHTML += ` | answered: ${answer}`
			}
		}
	}
	resultBox.append(resDiv)
})if (answer == correct) {
	resDiv.classList.add('bg-success')
	resDiv.innerHTML += ` answered: ${answer}`
} else {
	resDiv.classList.add('bg-danger')
	resDiv.innerHTML += ` | correct answer: ${correct}`
	resDiv.innerHTML += ` | answered: ${answer}`
}
}
}
resultBox.append(resDiv)
})
},
},