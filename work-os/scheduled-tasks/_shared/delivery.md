DELIVERY (do this every run)

1. Find today's date in America/Chicago time. Write dates as YYYY-MM-DD.
2. Memory first. Call the Artifact tool with action 'list' and limit 50. Pick the artifacts whose title begins with '{{PREFIX}}' and read {{LOOKBACK}} with action 'read'. Use them to avoid repeating what he has already seen and to say what is new or changed. If none exist, say this is the first run.
3. When the brief is finished, write it to the file /home/user/brief.html as a simple, clean web page: a <title> of exactly '{{PREFIX}} YYYY-MM-DD', one small <style> block (system font, a comfortable reading width, plain colors, no dark backgrounds), then the brief as headings (h1, h2), paragraphs, bullet lists, and links. No scripts, no images that need downloading, no external files. Publish it with the Artifact tool: file_path /home/user/brief.html, favicon '{{FAVICON}}', description one sentence saying what this brief is. Print the URL it returns.
4. Send exactly one mobile push notification with the PushNotification tool: the title line, then the two or three most important lines of the brief, then the artifact URL. Never send a push about tool failures or partial progress, and never send more than one.
5. Also print the complete brief as your final message, so it can be read inside the run.
6. If the Artifact tool fails, still print the complete brief as your final message and say at the top that publishing failed. Do not use Google Drive for anything.
