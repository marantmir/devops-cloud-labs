<!--
  <<< Author notes: Step 3 >>>
  Just a historic note: the previous version of this step forced the learner
  to write a pull request description,
  checked that `main` was the receiving branch,
  and that the file was named correctly.
-->

## Passo 3: Abrir um pull request

_Bom trabalho fazendo aquele commit! :sparkles:_

Agora que você fez uma alteração no projeto e criou um commit, é hora de compartilhar sua alteração proposta através de um pull request!

**O que é um pull request?**: A colaboração acontece em um _[pull request](https://docs.github.com/en/get-started/quickstart/github-glossary#pull-request)_. O pull request mostra as alterações no seu branch para outras pessoas e permite que elas aceitem, rejeitem ou sugiram alterações adicionais ao seu branch. Em uma comparação lado a lado, este pull request manterá as alterações que você acabou de fazer no seu branch e proporá aplicá-las ao branch `main` do projeto. Para mais informações sobre pull requests, consulte "[About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)".

### :keyboard: Atividade: Criar um pull request

Você pode ter notado após seu commit que uma mensagem foi exibida indicando seu recente push para seu branch e fornecendo um botão que diz **Compare & pull request**.

![screenshot of message and button](/images/compare-and-pull-request.png)

Para criar um pull request automaticamente, clique em **Compare & pull request** e pule para o passo 6 abaixo. Se você não clicar no botão, as instruções abaixo o guiarão pela configuração manual do pull request.

1. Click on the **Pull requests** tab in the header menu of your repository.
2. Click **New pull request**.
3. In the **base:** dropdown, make sure **main** is selected.
4. Select the **compare:** dropdown, and click `my-first-branch`.

   ![screenshot showing both branch selections](/images/pull-request-branches.png)

5. Click **Create pull request**.
6. Enter a title for your pull request. By default, the title will automatically be the name of your branch. For this exercise, let's edit the field to say `Add my first file`.
7. The next field helps you provide a description of the changes you made. Here, you can add a description of what you’ve accomplished so far. As a reminder, you have: created a new branch, created a file, and made a commit.

   ![screenshot showing pull request](/images/Pull-request-description.png)

8. Click **Create pull request**. You will automatically be navigated to your new pull request.
9. Wait about 20 seconds then refresh this page (the one you're following instructions from). [GitHub Actions](https://docs.github.com/en/actions) will automatically update to the next step.

> [!NOTE]
> Você pode ver evidências do GitHub Actions sendo executado na aba com o pull request aberto! A imagem abaixo mostra uma linha que você pode ver no seu pull request depois que a Action terminar de executar.
> 
> ![screenshot of an example of an actions line](/images/Actions-to-step-4.png)
