$(document).ready(function () {
    // Toggle chat button and chat box
    $('.chat-button').on('click', function () {
        $('.chat-button').css({ "display": "none" });
        $('.chat-box').css({ "visibility": "visible" });
    });

    $('.chat-box-header p').on('click', function () {
        $('.chat-button').css({ "display": "block" });
        $('.chat-box').css({ "visibility": "hidden" });
    });

    // Toggle modal
    $("#addExtra").on("click", function () {
        $(".modal").toggleClass("show-modal");
    });

    $(".modal-close-button").on("click", function () {
        $(".modal").toggleClass("show-modal");
    });

    // Chatbot functionality
    $('.send').on('click', sendMessage);
    $('#user-input').on('keypress', function (e) {
        if (e.which == 13) { // Enter key
            sendMessage();
        }
    });

    function sendMessage() {
        let userInput = $('#user-input').val().trim();
        if (userInput === "") return;

        // Add user's message to chat
        let userMessage = `
            <div class="chat-box-body-send">
                <p>${userInput}</p>
                <span>${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
            </div>`;
        $('.chat-box-body').append(userMessage);

        // Clear input
        $('#user-input').val("");

        // Bot response
        setTimeout(() => {
            let botResponse = getBotResponse(userInput.toLowerCase());
            let botMessage = `
                <div class="chat-box-body-receive">
                    <p>${botResponse}</p>
                    <span>${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
                </div>`;
            $('.chat-box-body').append(botMessage);

            // Auto-scroll to bottom
            $('.chat-box-body').scrollTop($('.chat-box-body')[0].scrollHeight);
        }, 1000); // Simulate typing delay
    }

    function getBotResponse(input) {
        // Simple Bangladesh history Q&A logic
        if (input.includes("independence") || input.includes("1971")) {
            return "Bangladesh gained independence from Pakistan on March 26, 1971, after a nine-month Liberation War. It was officially recognized as a sovereign nation on December 16, 1971, known as Victory Day.";
        } else if (input.includes("language movement") || input.includes("1952")) {
            return "The Language Movement of 1952 was a pivotal event in Bangladesh’s history. On February 21, 1952, students protested to establish Bengali as a state language, leading to martyrs and the eventual recognition of Bengali in 1956.";
        } else if (input.includes("partition") || input.includes("1947")) {
            return "The Partition of India in 1947 created East Pakistan (now Bangladesh) as part of Pakistan. It was separated from West Pakistan by over 1,000 miles of Indian territory.";
        } else if (input.includes("sheikh mujibur rahman") || input.includes("bangabandhu")) {
            return "Sheikh Mujibur Rahman, fondly called Bangabandhu, was the founding leader of Bangladesh. He led the independence movement and became the first President in 1971.";
        } else {
            return "I’m not sure about that! Ask me about Bangladesh’s independence, the Language Movement, or key figures like Sheikh Mujibur Rahman.";
        }
    }
});