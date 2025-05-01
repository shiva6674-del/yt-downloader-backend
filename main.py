<div style="background: url('https://img.freepik.com/free-psd/gradient-abstract-borders_23-2150602089.jpg?t=st=1746110644~exp=1746114244~hmac=138d65f33d5c853f80310392705fe16e5b20a9f080926ac538d7137cf6fe2bba&w=996'); background-size: cover; padding: 20px; border-radius: 12px; color: white; font-family: sans-serif;">
  <h2 style="text-align: center;">🎥 YouTube Video Downloader</h2>
  <input type="text" id="yt-url" placeholder="Paste YouTube URL here" style="width: 100%; padding: 10px; border-radius: 8px; border: none; margin-bottom: 10px;" />
  <select id="format" style="width: 100%; padding: 10px; border-radius: 8px; border: none; margin-bottom: 10px;">
    <option value="mp4">MP4 (Video)</option>
    <option value="mp3">MP3 (Audio)</option>
  </select>
  <button onclick="downloadYT()" style="width: 100%; padding: 12px; background: #ff5e57; color: white; border: none; border-radius: 8px; font-size: 16px;">Download</button>
  <p id="status" style="margin-top: 10px; text-align: center;"></p>
</div>

<script>
function downloadYT() {
  const url = document.getElementById('yt-url').value;
  const format = document.getElementById('format').value;
  const status = document.getElementById('status');

  if (!url) {
    status.innerText = '❌ Please enter a YouTube URL.';
    return;
  }

  status.innerText = '⏳ Processing...';

  fetch('https://yt-downloader.your-username.repl.co/download', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url: url, format: format })
  })
  .then(response => response.json())
  .then(data => {
    if (data.download_url) {
      status.innerHTML = `✅ <a href="${data.download_url}" target="_blank" style="color: yellow;">Click here to download</a>`;
    } else {
      status.innerText = '❌ Download failed.';
    }
  })
  .catch(() => {
    status.innerText = '❌ Server error.';
  });
}
</script>
