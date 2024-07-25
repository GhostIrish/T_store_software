[Setup]
AppName=ProjectTStore
AppVersion=1.0
DefaultDirName={pf}\ProjectTStore
DefaultGroupName=ProjectTStore
OutputDir=.
OutputBaseFilename=ProjectTStoreInstaller
Compression=lzma
SolidCompression=yes

[Files]
; Executáveis da GUI e da API
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion

; Scripts de configuração e inicialização
Source: "setup.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "setup.sh"; DestDir: "{app}"; Flags: ignoreversion

; Docker Compose e outros arquivos necessários
Source: "docker-compose.yml"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\ProjectTStore"; Filename: "{app}\main.exe"
Name: "{group}\Start API"; Filename: "{app}\app.exe"

[Run]
Filename: "{app}\setup.bat"; Description: "Configuring Database"; Flags: runhidden
Filename: "{app}\setup.sh"; Description: "Starting Application"; Flags: nowait postinstall
