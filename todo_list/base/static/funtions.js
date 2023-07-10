// function([string1, string2],target id,[color1,color2])    
consoleText(['Welcome to', 'Learn with', 'Do it with'], 'text', ['var(--links-color)', 'var(--links-color-disable)', 'var(--links-color-active)']);

function consoleText(words, id, colors) {
    if (colors === undefined) colors = ['#fff'];
    var visible = true;
    var con = document.getElementById('console');
    var letterCount = 1;
    var x = 1;
    var waiting = false;
    var target = document.getElementById(id)
    target.setAttribute('style', 'color:' + colors[0])
    window.setInterval(function () {
        if (letterCount === 0 && waiting === false) {
            waiting = true;
            target.innerHTML = words[0].substring(0, letterCount)
            window.setTimeout(function () {
                var usedColor = colors.shift();
                colors.push(usedColor);
                var usedWord = words.shift();
                words.push(usedWord);
                x = 1;
                target.setAttribute('style', 'color:' + colors[0])
                letterCount += x;
                waiting = false;
            }, 1000)
        } else if (letterCount === words[0].length + 1 && waiting === false) {
            waiting = true;
            window.setTimeout(function () {
                x = -1;
                letterCount += x;
                waiting = false;
            }, 1000)
        } else if (waiting === false) {
            target.innerHTML = words[0].substring(0, letterCount)
            letterCount += x;
        }
    }, 120)
    window.setInterval(function () {
        if (visible === true) {
            con.className = 'console-underscore hidden'
            visible = false;
        } else {
            con.className = 'console-underscore'
            visible = true;
        }
    }, 400)
}

function frase(){
    var aFrases=new Array();
    aFrases[0]=" “We cannot solve problems with the kind of thinking we employed when we came up with them.” — Albert Einstein";
    aFrases[1]=" “Be a light unto yourself; betake yourselves to no external refuge. Hold fast to the Truth. Look not for refuge to anyone besides yourselves.” ― Buddha Shakyamuni";
    aFrases[2]=" “Learn as if you will live forever, live like you will die tomorrow.” — Mahatma Gandhi";
    aFrases[3]=" “Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” ";
    aFrases[4]=" “Education is the most powerful weapon which you can use to change the world.” — Nelson Mandela";
    aFrases[5]=" “Just one small positive thought in the morning can change your whole day.” — Dalai Lama";
    aFrases[6]=" “If we learn to open our hearts, anyone, including the people who drive us crazy, can be our teacher.” ― Pema Chodron";
    aFrases[7]=" “Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.” — Buddha";
    aFrases[8]=" “Thousands of candles can be lighted from a single candle, and the life of the candle will not be shortened. Happiness never decreases by being shared.” — Buddha";
    aFrases[9]=" “An idea that is developed and put into action is more important than an idea that exists only as an idea.” — Buddha";
    aFrases[10]=" “Teach this triple truth to all: A generous heart, kind speech, and a life of service and compassion are the things which renew humanity.” — Buddha";
    
    var numRnd=Math.floor(Math.random()* aFrases.length);
    document.getElementById("fraseRandom").innerText=aFrases[numRnd];
    }
    
// modal
const myModal = document.getElementById('myModal')
const myInput = document.getElementById('myInput')

myModal.addEventListener('shown.bs.modal', () => {
  myInput.focus()
})

document.addEventListener('DOMContentLoaded', function() {
    var buttons = document.querySelectorAll('[data-bs-target="#modal1"]');
    var modalInfo = document.getElementById('modal-info');
  
    buttons.forEach(function(button) {
      button.addEventListener('click', function() {
        var info = this.getAttribute('data-info');
        modalInfo.textContent = info;
      });
    });
  });

// task form assign task
  function habilitarSelect() {
    var switchElement = document.getElementById('flexSwitchCheckDefault');
    var select = document.getElementById('selectOptions');
    
    select.disabled = !switchElement.checked; // Habilitar el select si el switch está marcado
  }