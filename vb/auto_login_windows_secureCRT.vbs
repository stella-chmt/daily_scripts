# $language = "VBScript"
# $interface = "1.0"
' Connect to an SSH server using the SSH2 protocol. Specify the
' username and password and hostname on the command line as well as
' some SSH2 protocol specific options.
Sub Main
   
  Dim passwd
  passwd = "YOURPASSWORD"
   
  Dim token
  token = "YOURTOKEN"
   
  Dim objShell
  Set objShell = CreateObject("WScript.Shell")
  cmd = "cmd /c totp -b " & token
  Set objExecObject = objShell.Exec(cmd)
  strText = ""
   
  select case objExecObject.status
    case wshFinished
            strText = objExecObject.StdOut.ReadAll
  end select
   
  crt.Screen.WaitForString "Verification code:"
  crt.Screen.Send strText & VbCr
  crt.Screen.WaitForString "Password:"
  crt.Screen.Send passwd & VbCr
  crt.Screen.Synchronous =False
End Sub