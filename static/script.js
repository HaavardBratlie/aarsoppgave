let currentQuestion = 1;
let score = 0;

function startQuiz() {
    document.getElementById("startButton").style.display = "none";
    document.getElementById("quizForm").style.display = "block";
    document.getElementById("question1").style.display = "block";
    document.getElementById("nextButton").style.display = "inline-block";
}

function answerQuestion(answer) {
    if (currentQuestion === 1 && answer === "Star Wars") {
        score++;
    }
    if (currentQuestion === 2 && answer === "Skrekk") {
        score++;
    }
    if (currentQuestion === 3 && answer === "Star Wars: Jedi Survivor") {
        score++;
    }
    if (currentQuestion === 4 && answer === "Fotball") {
        score++;
    }
    if (currentQuestion === 5 && answer === "21. September") {
        score++;
    }

    document.getElementById("question" + currentQuestion).style.display = "none";

    if (currentQuestion === 5) {
        const resultText = "Du fikk " + score + " av 5 riktig";
        document.getElementById("result").textContent = resultText;
        fetch('/submit_result', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'score=' + score
        });

        document.getElementById("nextButton").style.display = "none";
    } else {
        currentQuestion++;
        document.getElementById("question" + currentQuestion).style.display = "block";
    }
}

//-----------------------------------------------------

let currentQuestion2 = 1;
let score2 = 0;

function startQuiz2() {
    document.getElementById("startButton2").style.display = "none";
    document.getElementById("quizForm2").style.display = "block";
    document.getElementById("question2_1").style.display = "block";
    document.getElementById("nextButton2").style.display = "inline-block";
}

function answerQuestion2(answer) {
    if (currentQuestion2 === 1 && answer === "IT Utvikling") {
        score2++;
    }
    if (currentQuestion2 === 2 && answer === "HTML, css, js, flask") {
        score2++;
    }
    if (currentQuestion2 === 3 && answer === "Maria DB") {
        score2++;
    }

    document.getElementById("question2_" + currentQuestion2).style.display = "none";

    if (currentQuestion2 === 3) {
        const resultText2 = "Du fikk " + score2 + " av 3 riktig";
        document.getElementById("result").textContent = resultText2;
        fetch('/submit_result', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'score=' + score2
        });

        document.getElementById("nextButton2").style.display = "none";
    } else {
        currentQuestion2++;
        document.getElementById("question2_" + currentQuestion2).style.display = "block";
    }
}