import wmi

# Conectando ao WMI Service
w = wmi.WMI()

while True:
    menu = int(input(
        '''Escolha uma das opções:
        [1] Coletando Informações do Processador
        [2] Listando Processos em Execução
        [3] Monitorando o Uso de Memória
        [4] Controlando Serviços do Sistema
        [5] Monitorando Eventos em Tempo Real
        [6] Executando Consultas Personalizadas com WQL
        [0] Encerrar
        '''
    ))

    # 1.Coletando Informações do Processador
    if menu == 1:
        for processor in w.Win32_Processor():
            print(f"Nome do Processador: {processor.Name}")
            print(f"Número de Núcleos: {processor.NumberOfCores}")
            print(f"Frequência: {processor.MaxClockSpeed} MHz")


    # 2.Listando Processos em Execução
    elif menu == 2:
        for process in w.Win32_Process():
            print(f"ID do Processo: {process.ProcessId}, Nome: {process.Name}")


    # 3.Monitorando o Uso de Memória
    elif menu == 3:
        for os in w.Win32_OperatingSystem():
            total_mem = int(os.TotalVisibleMemorySize) // 1024
            free_mem = int(os.FreePhysicalMemory) // 1024
            print(f"Memória Total: {total_mem} MB")
            print(f"Memória Livre: {free_mem} MB")


    # 4.Controlando Serviços do Sistema
    elif menu == 4:
        for service in w.Win32_Service(Name="Spooler"):
            if service.State != "Running":
                result = service.StartService()
                print("Serviço Spooler iniciado" if result == 0 else "Falha ao iniciar o serviço")
            else:
                print("Serviço Spooler já está em execução")
                

    # 5.Monitorando Eventos em Tempo Real
    elif menu == 5:
        process_watcher = w.watch_for(notification_type="Creation", wmi_class="Win32_Process")
        print("Monitorando a criação de novos processos...")
        while True:
            new_process = process_watcher()
            print(f"Novo Processo Criado: {new_process.Caption} (PID: {new_process.ProcessId})")


    # 6.Executando Consultas Personalizadas com WQL
    elif menu == 6:
        processes = w.query("SELECT * FROM Win32_Process WHERE Name='fontdrvhost.exe'")
        for process in processes:
            print(f"Processo Encontrado: {process.Name} (PID: {process.ProcessId})")

    else:
        print("Opção inválida!")