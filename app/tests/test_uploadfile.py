import asyncio
import json
from playwright.async_api import async_playwright


async def load_cookies():
    """
    Carrega os cookies salvos para manter a sessão autenticada.

    :return: Lista de cookies carregados.
    """
    try:
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
        print(f"✅ {len(cookies)} Cookies carregados com sucesso!")
        return cookies
    except (FileNotFoundError, json.JSONDecodeError):
        print("❌ Erro ao carregar cookies. Execute primeiro save_cookies().")
        return None


async def setup_browser(p, cookies):
    """
    Configura o navegador e aplica os cookies.

    :param p: Instância do Playwright.
    :param cookies: Lista de cookies carregados.
    :return: Objeto `page` do navegador.
    """
    browser = await p.chromium.launch(headless=False)
    context = await browser.new_context()
    await context.add_cookies(cookies)
    page = await context.new_page()
    return browser, context, page


async def access_wetransfer(page, url):
    """
    Acessa o site do WeTransfer e verifica se o login foi restaurado corretamente.

    :param page: Objeto `page` do Playwright.
    :param url: URL do WeTransfer.
    :return: `True` se carregado corretamente, `False` caso contrário.
    """
    print("🔄 Acessando WeTransfer...")
    await page.goto(url, wait_until="load")

    if "wetransfer.com" not in page.url:
        print(f"❌ Erro ao carregar WeTransfer. Página atual: {page.url}")
        return False

    print("✅ WeTransfer carregado com sucesso!")
    return True


async def handle_popups(page):
    """
    Aceita cookies e termos de serviço, caso esses pop-ups apareçam.

    :param page: Objeto `page` do Playwright.
    """
    try:
        await page.click("button:has-text('Accept All')")
        print("✅ Cookies aceitos")
    except:
        print("🚀 Nenhum pop-up de cookies encontrado!")

    try:
        await page.click("button:has-text('I agree')")
        print("✅ Termos de serviço aceitos")
    except:
        print("✅ Termos de serviço já aceitos!")


async def upload_file(page, file_path):
    """
    Localiza o input de upload, torna-o visível e faz o upload do arquivo.

    :param page: Objeto `page` do Playwright.
    :param file_path: Caminho do arquivo a ser enviado.
    """
    await page.wait_for_selector("input[data-testid='file-input']", timeout=20000)
    print("📂 Input de upload encontrado!")

    await page.evaluate("""
        const input = document.querySelector("input[data-testid='file-input']");
        input.style.display = 'block';
        input.style.visibility = 'visible';
        input.style.opacity = '1';
        input.style.pointerEvents = 'auto';
        input.removeAttribute('aria-hidden');
    """)
    await asyncio.sleep(2)

    file_input = page.locator("input[data-testid='file-input']").first
    await file_input.set_input_files(file_path, timeout=15000)
    print(f"📂 Arquivo '{file_path}' carregado com sucesso!")


async def fill_transfer_details(page, sender_email, recipient_email, transfer_title, transfer_message):
    """
    Preenche os detalhes do envio no WeTransfer.
    """

    # 📩 Preencher o e-mail do remetente
    try:
        await page.wait_for_selector("input[name='autosuggest']", state="visible", timeout=10000)
        await page.fill("input[name='autosuggest']", sender_email)
        print("📩 E-mail do remetente preenchido!")
    except Exception as e:
        print(f"❌ Erro ao preencher o e-mail do remetente: {e}")

    # 📩 Preencher o e-mail do destinatário
    try:
        email_inputs = page.locator("input[name='email']")
        await email_inputs.nth(0).fill(recipient_email)
        print("ok")
    except Exception as e:
        print(f"❌ Erro ao preencher o e-mail do destinatário: {e}")

    # 📝 Preencher o título do envio
    try:
        await page.wait_for_selector("input[name='displayName']", state="visible", timeout=5000)
        await page.fill("input[name='displayName']", transfer_title)
        print("📝 Título preenchido!")
    except Exception as e:
        print(f"❌ Erro ao preencher o título: {e}")

    # 💬 Preencher a mensagem
    try:
        await page.wait_for_selector("textarea[name='message']", state="visible", timeout=5000)
        await page.fill("textarea[name='message']", transfer_message)
        print("💬 Mensagem preenchida!")
    except Exception as e:
        print(f"❌ Erro ao preencher a mensagem: {e}")




async def start_transfer(page):
    """
    Inicia a transferência do arquivo clicando no botão 'Transfer'.

    :param page: Objeto `page` do Playwright.
    """
    await page.click("button:has-text('Transfer')")
    print("🚀 Upload iniciado!")

    await page.screenshot(path="upload_success_ofc.png")
    print("📸 Screenshot salva como 'upload_success.png'")


async def main():
    """
    Função principal que executa o pipeline de envio de arquivo para o WeTransfer.
    """

    # 🔹 Configurações do envio
    file_path = "excel.xlsx"
    upload_url = "https://wetransfer.com/"
    sender_email = "vitoriarntrindade@gmail.com"
    recipient_email = "vitoria.raymara.tatix@gmail.com"
    transfer_title = "Relatório de Produtos"
    transfer_message = "Segue o relatório atualizado dos produtos."

    async with async_playwright() as p:
        # 🔹 1. Carregar cookies
        cookies = await load_cookies()
        if not cookies:
            return

        # 🔹 2. Configurar navegador
        browser, context, page = await setup_browser(p, cookies)

        # 🔹 3. Acessar WeTransfer
        success = await access_wetransfer(page, upload_url)
        if not success:
            await browser.close()
            return

        # 🔹 4. Aceitar cookies e termos, se necessário
        await handle_popups(page)

        # 🔹 5. Upload do arquivo
        await upload_file(page, file_path)

        # 🔹 6. Preencher os dados do envio
        await fill_transfer_details(page, sender_email, recipient_email, transfer_title, transfer_message)

        # 🔹 7. Iniciar a transferência
        await start_transfer(page)

        # 🔹 8. Finalizar sessão
        await asyncio.sleep(5)
        await browser.close()


# 🚀 Executar o pipeline
asyncio.run(main())
