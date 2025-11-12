// MZ/X 4.5 Fusion³D Core - Voice modul
// Feladata: magyar nyelvű hangos visszajelzések biztosítása az AI eseményeihez

console.log("[Voice] Modul betöltve – AI hanginterfész aktív.");

let voiceEnabled = true;
let currentVoice = null;

// === Hang inicializálása ===
function initVoice() {
  const voices = window.speechSynthesis.getVoices();
  currentVoice = voices.find(v => v.lang === "hu-HU") || voices[0];
  if (!currentVoice) console.warn("[Voice] Magyar hang nem található, alapértelmezett hang használatban.");
}

// === Szöveg felolvasása magyarul ===
function speakHU(text, rate = 1.0, pitch = 1.0) {
  if (!voiceEnabled) return;

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "hu-HU";
  utterance.rate = rate;
  utterance.pitch = pitch;
  utterance.voice = currentVoice;

  window.speechSynthesis.speak(utterance);
  console.log(`[Voice] Felolvasva: ${text}`);
}

// === Hang vezérlések ===
function toggleVoice() {
  voiceEnabled = !voiceEnabled;
  const state = voiceEnabled ? "bekapcsolva" : "kikapcsolva";
  console.log(`[Voice] Hang ${state}.`);
  showAIMessage(`🎙️ AI hang ${state}.`, "info");
}

function testVoice() {
  speakHU("MZ X négy pont öt fúziós intelligencia rendszer elindult.", 1.0, 1.0);
}

// === Hang események a böngészőben ===
window.speechSynthesis.onvoiceschanged = initVoice;

// === Automatikus tesztindítás (eltávolítható) ===
setTimeout(() => {
  testVoice();
  showAIMessage("AI hangmodul aktiválva.", "success");
}, 2000);
