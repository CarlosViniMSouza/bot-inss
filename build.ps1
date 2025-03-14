$exclude = @("venv", "bot_test_tj.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_test_tj.zip" -Force