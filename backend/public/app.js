document.getElementById("fetch").onclick = async () => {
  const out = document.getElementById("output");
  out.innerText = "Kérlek várj, lekérdezés...";
  const res = await fetch("/ai/signal?symbol=BTCUSDT");
  const data = await res.json();
  out.innerHTML = `
    <h3>${data.symbol}</h3>
    <p><b>AI jelzés:</b> ${data.signal}</p>
    <p><b>Bias:</b> ${data.bias}</p>`;
  document.getElementById("status").innerText = "✅ Frissítve";
};
