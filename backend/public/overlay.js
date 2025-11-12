// MZ/X 4.5 Fusion³D Core - Overlay modul
// Feladata: AI-üzenetek és rendszerállapot vizuális megjelenítése a képernyőn

console.log("[Overlay] Modul betöltve – AI-üzenet overlay aktív.");

// === Overlay létrehozása ===
const overlayContainer = document.createElement("div");
overlayContainer.id = "ai-overlay";
overlayContainer.style.position = "fixed";
overlayContainer.style.bottom = "20px";
overlayContainer.style.right = "20px";
overlayContainer.style.width = "360px";
overlayContainer.style.maxHeight = "50vh";
overlayContainer.style.overflowY = "auto";
overlayContainer.style.zIndex = "9999";
overlayContainer.style.padding = "10px";
overlayContainer.style.background = "rgba(15, 15, 25, 0.6)";
overlayContainer.style.border = "1px solid rgba(0, 255, 230, 0.4)";
overlayContainer.style.borderRadius = "12px";
overlayContainer.style.fontFamily = "Orbitron, monospace";
overlayContainer.style.color = "#00FFE0";
overlayContainer.style.fontSize = "14px";
overlayContainer.style.backdropFilter = "blur(8px)";
overlayContainer.style.boxShadow = "0 0 12px rgba(0,255,255,0.25)";
document.body.appendChild(overlayContainer);

// === Üzenet megjelenítése ===
function showAIMessage(msg, level = "info") {
  const entry = document.createElement("div");
  entry.style.marginBottom = "6px";
  entry.style.padding = "6px 10px";
  entry.style.borderRadius = "8px";
  entry.style.opacity = "0";
  entry.style.transition = "opacity 0.5s ease-in-out";

  // Színezés szintenként
  if (level === "success") entry.style.color = "#00ff99";
  if (level === "warn") entry.style.color = "#ffcc00";
  if (level === "error") entry.style.color = "#ff4444";

  // Ikonok
  const prefix = {
    info: "🧠",
    success: "⚡",
    warn: "⚠️",
    error: "❌"
  }[level] || "💬";

  entry.textContent = `${prefix} ${msg}`;
  overlayContainer.prepend(entry);

  // Fokozatos megjelenítés
  requestAnimationFrame(() => (entry.style.opacity = "1"));

  // Automatikus eltűnés
  setTimeout(() => {
    entry.style.opacity = "0";
    setTimeout(() => entry.remove(), 500);
  }, 10000);
}

// === Tesztüzenetek (eltávolítható később) ===
showAIMessage("MZ/X 4.5 Fusion³D Core elindult ✅", "success");
showAIMessage("Élő adatfolyam inicializálva...", "info");
showAIMessage("Bias érték változik: +0.023 → semleges zóna", "warn");
