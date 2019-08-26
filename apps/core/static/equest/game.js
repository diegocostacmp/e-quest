
// using jQuery to generate csrf_token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// New game 
$('#game-create').click(function() {
    bookGame();
});

function bookGame() {
    //token de sessao
    var csrftoken = getCookie('csrftoken');

    // Get data select
    $.ajax({
        headers: { 'X-CSRFToken': csrftoken },
        type: 'POST',
        url: $("#game-create").attr("eg-url"),

        success: function(data) {
            var options = {};

            $.map(data,
                function(o) {
                    options[o.uuid] = o.discipline;
                });

            const { value: opt } = Swal.fire({
                title: 'Selecione uma disciplina',
                input: 'select',
                inputOptions: options,
                inputPlaceholder: 'Selecione uma disciplina',
                inputAttributes: {
                    autocapitalize: 'off'
                },
                showCancelButton: true,
                showLoaderOnConfirm: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: '<i class="fa fa-check"></i> Buscar!',
                cancelButtonText: '<i class="fa fa-times"></i> Cancelar',
                inputValidator: (value) => {
                    if (!value) {
                        return 'Selecione uma disciplina!'
                    }
                },
                preConfirm: (value) => {
                    window.location = '/game/game_create/' + value + '/';
                },
            })

        },
        error: function() {
            alert('deu erro');
        }
    });

}

//Show timer
function managerTime(){
    $("#timerQuestion").show()
    $(".play").trigger('click');
}


function callQuestion(){
    var questionPrincipal, urlDestiny;
    questionPrincipal = $('#questionPrincipal').val();
    urlDestiny = $("#questionPrincipal").attr("eg-url");
    csrftoken = getCookie('csrftoken');

    $.ajax({
        headers : {'X-CSRFToken': csrftoken},
        type    : 'POST',
        assync  : true,
        crossDomain: true,
        url     : urlDestiny,
        data    : {
            'question_principal': questionPrincipal
        },
        datatype: 'json',

        success: function(data) {
            $("#accordionExample6").append(data);
            var uuidUpdate = $('.card').last().attr('id');
            $("#questionPrincipal").val(uuidUpdate);
        },
        error: function(){
            Swal.fire({
                type: 'error',
                title: 'Desculpe...',
                text: 'Existem dependências associadas!'
            })
        }
    });
}

//circle start
let progressBar = document.querySelector('.e-c-progress');
let indicator = document.getElementById('e-indicator');
let pointer = document.getElementById('e-pointer');
let length = Math.PI * 2 * 100;

progressBar.style.strokeDasharray = length;

function update(value, timePercent) {
    var offset = -length - length * value / (timePercent);
    progressBar.style.strokeDashoffset = offset;
    pointer.style.transform = `rotate(${360 * value / (timePercent)}deg)`;
};

//circle ends
const displayOutput = document.querySelector('.display-remain-time')
const pauseBtn = document.getElementById('pause');
const setterBtns = document.querySelectorAll('button[data-setter]');

let intervalTimer;
let timeLeft;

// Timer total
let wholeTime = (5 / 60) * 60;
let isPaused = false;
let isStarted = false;


update(wholeTime, wholeTime); //refreshes progress bar
displayTimeLeft(wholeTime);

function changeWholeTime(seconds) {
    if ((wholeTime + seconds) > 0) {
        wholeTime += seconds;
        update(wholeTime, wholeTime);
    }
}

for (var i = 0; i < setterBtns.length; i++) {
    setterBtns[i].addEventListener("click", function(event) {
        var param = this.dataset.setter;
        switch (param) {
            case 'minutes-plus':
                changeWholeTime(1 * 60);
                break;
            case 'minutes-minus':
                changeWholeTime(-1 * 60);
                break;
            case 'seconds-plus':
                changeWholeTime(1);
                break;
            case 'seconds-minus':
                changeWholeTime(-1);
                break;
        }
        displayTimeLeft(wholeTime);
    });
}

function timer(seconds) { //counts time, takes seconds
    let remainTime = Date.now() + (seconds * 1000);
    displayTimeLeft(seconds);

    intervalTimer = setInterval(function() {
        timeLeft = Math.round((remainTime - Date.now()) / 1000);
        if (timeLeft < 0) {
            clearInterval(intervalTimer);
            isStarted = false;
            setterBtns.forEach(function(btn) {
                btn.disabled = false;
                btn.style.opacity = 1;
            });
            displayTimeLeft(wholeTime);
            pauseBtn.classList.remove('pause');
            pauseBtn.classList.add('play');
            $("#timerQuestion").hide();
            callQuestion();

            
            return;
        }
        displayTimeLeft(timeLeft);
    }, 1000);
}

function pauseTimer(event) {
    if (isStarted === false) {
        timer(wholeTime);
        isStarted = true;
        this.classList.remove('play');
        this.classList.add('pause');

        setterBtns.forEach(function(btn) {
            btn.disabled = true;
            btn.style.opacity = 0.5;
        });

    } else if (isPaused) {
        this.classList.remove('play');
        this.classList.add('pause');
        timer(timeLeft);
        isPaused = isPaused ? false : true
    } else {
        this.classList.remove('pause');
        this.classList.add('play');
        clearInterval(intervalTimer);
        isPaused = isPaused ? false : true;
    }
}

function displayTimeLeft(timeLeft) { //displays time on the input
    let minutes = Math.floor(timeLeft / 60);
    let seconds = timeLeft % 60;
    let displayString = `${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    displayOutput.textContent = displayString;
    update(timeLeft, wholeTime);
}

pauseBtn.addEventListener('click', pauseTimer);