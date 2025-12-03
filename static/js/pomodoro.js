// static/js/pomodoro.js
// Simple Pomodoro timer - works with pomodoro/templates/pomodoro.html

// Settings (in seconds)
let workMinutes = 25;
let breakMinutes = 5;
let remainingSeconds = workMinutes * 60;
let mode = 'work';  // 'work' or 'break'
let timer = null;

// DOM elements
const displayEl = document.getElementById('time-display');
const modeEl = document.getElementById('mode-label');
const startBtn = document.getElementById('start-btn');
const pauseBtn = document.getElementById('pause-btn');
const resetBtn = document.getElementById('reset-btn');
const presetBtns = document.querySelectorAll('.preset-btn');

// Helper: update the MM:SS text and mode label
function updateDisplay() {
  const minutes = Math.floor(remainingSeconds / 60);
  const seconds = remainingSeconds % 60;
  const mm = String(minutes).padStart(2, '0');
  const ss = String(seconds).padStart(2, '0');
  displayEl.textContent = `${mm}:${ss}`;
  modeEl.textContent = (mode === 'work') ? 'Work' : 'Break';
}

// Start timer (1-second ticks)
function startTimer() {
  if (timer !== null) return; // already running
  startBtn.disabled = true;
  pauseBtn.disabled = false;

  timer = setInterval(() => {
    remainingSeconds = remainingSeconds - 1;
    updateDisplay();

    if (remainingSeconds <= 0) {
      clearInterval(timer);
      timer = null;
      startBtn.disabled = false;
      pauseBtn.disabled = true;

      if (mode === 'work') {
        mode = 'break';
        remainingSeconds = breakMinutes * 60;
        updateDisplay();
        alert("Work session finished — time for a break!");
      } else {
        mode = 'work';
        remainingSeconds = workMinutes * 60;
        updateDisplay();
        alert("Break finished — ready for the next work session!");
      }
    }
  }, 1000);
}

// Pause
function pauseTimer() {
  if (timer === null) return;
  clearInterval(timer);
  timer = null;
  startBtn.disabled = false;
  pauseBtn.disabled = true;
}

// Reset to current mode default
function resetTimer() {
  if (timer !== null) {
    clearInterval(timer);
    timer = null;
  }
  startBtn.disabled = false;
  pauseBtn.disabled = true;
  if (mode === 'work') {
    remainingSeconds = workMinutes * 60;
  } else {
    remainingSeconds = breakMinutes * 60;
  }
  updateDisplay();
}

// Apply a preset (work / break minutes)
function setPreset(w, b) {
  workMinutes = parseInt(w, 10);
  breakMinutes = parseInt(b, 10);
  mode = 'work';
  remainingSeconds = workMinutes * 60;
  if (timer !== null) {
    clearInterval(timer);
    timer = null;
  }
  startBtn.disabled = false;
  pauseBtn.disabled = true;
  updateDisplay();
}

// Wire up events
startBtn.addEventListener('click', startTimer);
pauseBtn.addEventListener('click', pauseTimer);
resetBtn.addEventListener('click', resetTimer);

presetBtns.forEach((btn) => {
  btn.addEventListener('click', () => {
    const w = btn.getAttribute('data-work');
    const b = btn.getAttribute('data-break');
    setPreset(w, b);
  });
});

// Initialize display on page load
updateDisplay();