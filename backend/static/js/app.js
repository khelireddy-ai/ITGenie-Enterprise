// ===============================
// ITGenie Enterprise Chat
// ===============================

const chatBox = document.getElementById("chatBox");
const input = document.getElementById("question");

// -------------------------------
// Enter Key Support
// -------------------------------

input.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {

        askQuestion();

    }

});


// -------------------------------
// Suggested Question
// -------------------------------

function fillQuestion(text) {

    input.value = text;

    askQuestion();

}


// -------------------------------
// Main Function
// -------------------------------

async function askQuestion() {

    let question = input.value.trim();

    if (question === "") return;


    // User Bubble

    chatBox.innerHTML += `

    <div class="user-message">

        ${question}

    </div>

    `;


    // Loading Bubble

    chatBox.innerHTML += `

    <div class="bot-message" id="loading">

        <h3>🤖 ITGenie</h3>

        <div class="loading">

            <span></span>

            <span></span>

            <span></span>

        </div>

        <p>Thinking...</p>

    </div>

    `;

    scrollBottom();

    input.value = "";


    try {

        const response = await fetch("/ask", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                question: question

            })

        });


        const data = await response.json();


        // Remove Loading

        document.getElementById("loading").remove();


        // Add AI Response

        chatBox.innerHTML += createAnswerCard(data);


    }

    catch (err) {

        document.getElementById("loading").remove();

        chatBox.innerHTML += `

        <div class="bot-message">

            <h3>❌ Error</h3>

            <p>

                Unable to connect to ITGenie API.

            </p>

        </div>

        `;

    }

    scrollBottom();

}



// -------------------------------
// Build Response Card
// -------------------------------

function createAnswerCard(data) {

    return `

    <div class="bot-message">

        <h3>🤖 ITGenie</h3>

        <div class="answer-card">

            <h3>📘 Answer</h3>

            <p>

${escapeHtml(data.answer)}

            </p>

        </div>


        <div class="source">

            📄 <b>Source:</b>

            ${data.source}

        </div>


        <br>


        <button onclick="copyAnswer(this)"

        class="copy-btn">

            📋 Copy

        </button>


    </div>

    `;

}



// -------------------------------
// Copy Button
// -------------------------------

function copyAnswer(button) {

    const answer = button.parentElement.querySelector(".answer-card p").innerText;

    navigator.clipboard.writeText(answer);

    button.innerHTML = "✅ Copied";

    setTimeout(function () {

        button.innerHTML = "📋 Copy";

    }, 1500);

}



// -------------------------------
// Scroll Bottom
// -------------------------------

function scrollBottom() {

    chatBox.scrollTop = chatBox.scrollHeight;

}



// -------------------------------
// Escape HTML
// -------------------------------

function escapeHtml(text) {

    if (!text) return "";

    return text

        .replace(/&/g, "&amp;")

        .replace(/</g, "&lt;")

        .replace(/>/g, "&gt;")

        .replace(/\n/g, "<br>");

}



// -------------------------------
// Welcome Message
// -------------------------------

window.onload = function () {

    scrollBottom();

};
