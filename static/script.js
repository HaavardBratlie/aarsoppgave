let currentQuestion = 1;
let score = 0;
let userAnswers = [];
let correctAnswers = ["Star Wars", "Skrekk", "Star Wars: Jedi Survivor", "Fotball", "21. September"];

function startQuiz() {
    document.getElementById("startButton").style.display = "none";
    document.getElementById("quizForm").style.display = "block";
    document.getElementById("question1").style.display = "block";
    document.getElementById("nextButton").style.display = "inline-block";
}

function answerQuestion(answer) {
    userAnswers[currentQuestion - 1] = answer;

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
        showResults();
    } else {
        currentQuestion++;
        document.getElementById("question" + currentQuestion).style.display = "block";
    }
}

function showResults() {
    const resultContainer = document.getElementById("result");
    resultContainer.style.display = "block";
    resultContainer.innerHTML = "";

    const resultText = "Du fikk " + score + " av 5 riktig";
    resultContainer.innerHTML += `<h2>${resultText}</h2>`;

    for (let i = 0; i < correctAnswers.length; i++) {
        const questionResult = document.createElement("p");
        if (userAnswers[i] === correctAnswers[i]) {
            questionResult.innerHTML = `✅ ${i + 1}: Du svarte '${userAnswers[i]}'`;
            questionResult.style.color = "green";
        } else {
            questionResult.innerHTML = `❌ ${i + 1}: Du svarte '${userAnswers[i]}' (Riktig svar: '${correctAnswers[i]}')`;
            questionResult.style.color = "red";
        }
        resultContainer.appendChild(questionResult);
    }

    fetch('/submit_result', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'score=' + score
    });

    document.getElementById("nextButton").style.display = "none";
}

let currentQuestion2 = 1;
let score2 = 0;
let userAnswers2 = [];
let correctAnswers2 = ["IT Utvikling", "HTML, css, js, flask", "Maria DB"];

function startQuiz2() {
    document.getElementById("startButton2").style.display = "none";
    document.getElementById("quizForm2").style.display = "block";
    document.getElementById("question2_1").style.display = "block";
    document.getElementById("nextButton2").style.display = "inline-block";
}

function answerQuestion2(answer) {
    userAnswers2[currentQuestion2 - 1] = answer;

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
        showResults2();
    } else {
        currentQuestion2++;
        document.getElementById("question2_" + currentQuestion2).style.display = "block";
    }
}

function showResults2() {
    const resultContainer2 = document.getElementById("result2");
    resultContainer2.style.display = "block";
    resultContainer2.innerHTML = "";

    const resultText2 = "Du fikk " + score2 + " av 3 riktig";
    resultContainer2.innerHTML += `<h2>${resultText2}</h2>`;

    for (let i = 0; i < correctAnswers2.length; i++) {
        const questionResult2 = document.createElement("p");
        if (userAnswers2[i] === correctAnswers2[i]) {
            questionResult2.innerHTML = `✅ ${i + 1}: Du svarte '${userAnswers2[i]}'`;
            questionResult2.style.color = "green";
        } else {
            questionResult2.innerHTML = `❌ ${i + 1}: Du svarte '${userAnswers2[i]}' (Riktig svar: '${correctAnswers2[i]}')`;
            questionResult2.style.color = "red";
        }
        resultContainer2.appendChild(questionResult2);
    }

    fetch('/submit_result2', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'score=' + score2
    });

    document.getElementById("nextButton2").style.display = "none";
}