// Simple Pomodoro timer - works with pomodoro/templates/pomodoro.html

// Settings (in seconds)
let workMinutes = 1; // SET BACK TO 25 ONCE BUGS ARE CLEARED
let breakMinutes = 1; // SET BACK TO 5 ONCE BUGS ARE CLEARED
let remainingSeconds = workMinutes * 60;
let mode = 'work';  // 'work' or 'break'
let timer = null;

// DECLARE variables globally (assigning them in DOMContentLoaded block below)
let displayEl;
let modeEl;
let toggleBtn;
let resetBtn;
let presetBtns;
let notificationSound;

// Helper: update the MM:SS text and mode label
function updateDisplay() {
  const minutes = Math.floor(remainingSeconds / 60);
  const seconds = remainingSeconds % 60;
  const mm = String(minutes).padStart(2, '0');
  const ss = String(seconds).padStart(2, '0');
  displayEl.textContent = `${mm}:${ss}`;
  
  // Dynamic Color Based on Work/Brake mode
  if (mode === 'work') {
    modeEl.textContent = 'Work';
    modeEl.classList.remove('bg-primary', 'text-white');
    modeEl.classList.add('bg-light', 'text-dark');
  } else {
    modeEl.textContent = 'Break';
    modeEl.classList.remove('bg-light', 'text-dark');
    modeEl.classList.add('bg-primary', 'text-white');
  }
}

// Start timer (1-second ticks)
function startTimer() {
  if (timer !== null) return; // already running
  toggleBtn.innerHTML = '<i class="fa-solid fa-pause me-1"></i>Pause';
  toggleBtn.classList.replace('btn-primary', 'btn-warning');
  toggleBtn.classList.replace('btn-success', 'btn-warning');
  resetBtn.disabled = false;

  timer = setInterval(() => {
    remainingSeconds = remainingSeconds - 1;
    updateDisplay();

    if (remainingSeconds <= 0) {
      clearInterval(timer);
      timer = null;
      toggleBtn.innerHTML = '<i class="fa-solid fa-play me-1"></i>Start';
      toggleBtn.classList.replace('btn-warning', 'btn-success');
      resetBtn.disabled = false;
      // Play bell sound
      notificationSound.play();

      // Auto-start the break timer
      startTimer(); 
      if (mode === 'work') {
        mode = 'break';
        remainingSeconds = breakMinutes * 60;
        updateDisplay();
      } else {
        mode = 'work';
        remainingSeconds = workMinutes * 60;
        updateDisplay();
      }
    }
  }, 1000);
}

// Pause
function pauseTimer() {
  if (timer === null) return;
  clearInterval(timer);
  timer = null;
  toggleBtn.innerHTML = '<i class="fa-solid fa-play me-1"></i>Resume';
  toggleBtn.classList.replace('btn-warning', 'btn-success');
}

// Toggle function to manage Start/Pause states:
function toggleTimer() {
    if (timer !== null) {
        // Timer is running, so pause it
        pauseTimer();
    } else {
        // Timer is stopped/paused, so start it
        startTimer();
    }
}

// Reset to current mode default
function resetTimer() {
  if (timer !== null) {
    clearInterval(timer);
    timer = null;
  }
  toggleBtn.innerHTML = '<i class="fa-solid fa-play me-1"></i>Start';
  toggleBtn.classList.replace('btn-warning', 'btn-success');
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
  toggleBtn.innerHTML = '<i class="fa-solid fa-play me-1"></i>Start';
  toggleBtn.classList.replace('btn-warning', 'btn-success');
  updateDisplay();
}

// Ensure the script runs only after the HTML elements are fully loaded

document.addEventListener('DOMContentLoaded', function() {
  // Assign DOM elements, guaranteeing they exist
  displayEl = document.getElementById('time-display');
  modeEl = document.getElementById('mode-label');
  toggleBtn = document.getElementById('toggle-btn');
  resetBtn = document.getElementById('reset-btn');
  presetBtns = document.querySelectorAll('.preset-btn');
  notificationSound = document.getElementById('notification-sound');
  
  // Wire up events
  toggleBtn.addEventListener('click', toggleTimer);
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
});
