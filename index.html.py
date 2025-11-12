# === SignalHive — Flask demo for Pydroid3 ===
# Run: python app.py
# Then open: http://127.0.0.1:5000

from flask import Flask, render_template_string
app = Flask(__name__)

html = """<!doctype html>
<html lang='en'>
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <title>SignalHive - AI Automations & Live Signals</title>
  <script src='https://cdn.tailwindcss.com'></script>
  <style>.card{background:white;border-radius:12px;box-shadow:0 6px 20px rgba(8,15,30,0.06);}</style>
</head>
<body class='bg-gray-50 text-gray-800 font-sans'>
<header class='max-w-6xl mx-auto p-6 flex items-center justify-between'>
  <h1 class='text-2xl font-bold text-indigo-600'>SignalHive</h1>
  <nav class='space-x-4 text-sm'>
    <a href='#products' class='text-indigo-600'>Products</a>
    <a href='#signals' class='text-gray-600'>Signals</a>
  </nav>
</header>

<main class='max-w-6xl mx-auto p-6'>
  <section>
    <h2 class='text-3xl font-extrabold'>AI Automations & Live Signals</h2>
    <p class='mt-2 text-gray-600'>Demo web app served from Flask. Replace demo parts with your real API endpoints or signal feeds.</p>
  </section>

  <section id='products' class='mt-8 grid sm:grid-cols-2 lg:grid-cols-3 gap-6'>
    <div class='card p-5'>
      <h3 class='font-semibold'>BTC 60-Second Signals</h3>
      <p class='text-sm text-gray-600 mt-2'>High-frequency BTC signal feed for short-term trading.</p>
      <div class='mt-3 flex justify-between items-center'>
        <div class='font-bold'>$19 / mo</div>
        <button class='px-3 py-2 bg-indigo-600 text-white rounded'>Buy</button>
      </div>
    </div>

    <div class='card p-5'>
      <h3 class='font-semibold'>AI Trade Automator</h3>
      <p class='text-sm text-gray-600 mt-2'>Automates orders via broker API. Replace demo placeholders.</p>
      <div class='mt-3 flex justify-between items-center'>
        <div class='font-bold'>$49 one-time</div>
        <button class='px-3 py-2 bg-indigo-600 text-white rounded'>Buy</button>
      </div>
    </div>
  </section>

  <section id='signals' class='mt-10 card p-6'>
    <h3 class='font-semibold'>Live Signal Feed (demo)</h3>
    <div id='signalBox' class='mt-4 p-3 border rounded bg-gray-50'>No connection yet</div>
    <div class='mt-4 flex gap-2'>
      <input id='wsUrl' class='flex-1 p-2 border rounded' placeholder='wss://your-signal-server.example'>
      <button id='connectBtn' class='px-3 py-2 bg-green-600 text-white rounded'>Connect</button>
    </div>
  </section>
</main>

<footer class='max-w-6xl mx-auto p-6 text-xs text-gray-500 text-center'>
  © SignalHive demo. Replace with production keys before publishing.
</footer>

<script>
  let ws;
  document.getElementById('connectBtn').addEventListener('click', ()=>{
    const url=document.getElementById('wsUrl').value.trim();
    const box=document.getElementById('signalBox');
    if(!url){alert('Enter WebSocket URL');return;}
    if(ws) ws.close();
    ws=new WebSocket(url);
    box.innerText='Connecting...';
    ws.onopen=()=>box.innerText='Connected — waiting for signals...';
    ws.onmessage=(e)=>{
      try{
        const d=JSON.parse(e.data);
        box.innerText=`${d.symbol} ${d.side} @ ${d.price}`;
      }catch{ box.innerText=e.data; }
    };
    ws.onclose=()=>box.innerText='Disconnected';
    ws.onerror=()=>box.innerText='Error connecting';
  });
</script>
</body>
</html>"""

@app.route('/')
def home():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)