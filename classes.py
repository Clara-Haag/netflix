class Serie:
    def __init__(self, titulo, imagem, sinopse, temporadas, avaliacao, elenco):
        self.titulo = titulo
        self.imagem = imagem
        self.sinopse = sinopse
        self.temporadas = temporadas
        self.avaliacao = avaliacao
        self.elenco = elenco

class Tema:
    def __init__(self, nome):
        self.nome = nome
        self.series = []

    def adicionar_serie(self, serie):
        self.series.append(serie)

# criação das séries e dos temas
tema_suspense = Tema("Suspense")

serie_stranger_things = Serie("Stranger Things", "strangerthings.jpg", "Quando Will Byers desaparece misteriosamente, seus amigos iniciam uma busca pelo garoto, descobrindo experimentos secretos, forças sobrenaturais e uma garota estranha com poderes telecinéticos.", 4, "4.5 estrelas", "Millie Bobby Brown, Finn Wolfhard")
tema_suspense.adicionar_serie(serie_stranger_things)

serie_dark = Serie("Dark", "dark.jpg", "Em uma cidade pequena, desaparecimentos inexplicáveis ​​levam quatro famílias a uma busca frenética por respostas enquanto tentam desvendar um mistério que abrange três gerações.", 3, "4.8 estrelas", "Louis Hofmann, Oliver Masucci")
tema_suspense.adicionar_serie(serie_dark)

serie_narcos = Serie("Narcos", "narcos.jpg", "Baseada na história real do narcotraficante Pablo Escobar, essa série retrata a vida do poderoso chefão do tráfico e as forças policiais e políticas que tentam capturá-lo.", 5, "4.7 estrelas", "Wagner Moura, Pedro Pascal")
tema_suspense.adicionar_serie(serie_narcos)

tema_policial = Tema("Policial")

serie_lupin = Serie("Lupin", "lupin.jpg", "Em Paris, o ladrão profissional Assane Diop busca vingança pelo injusto tratamento de seu pai, e usa as habilidades de ladrão para expor os crimes da elite.", 2, "4.6 estrelas", "Omar Sy, Ludivine Sagnier")
tema_policial.adicionar_serie(serie_lupin)

serie_casa_de_papel = Serie("La Casa de Papel", "lacasadepapel.jpeg", "Oito ladrões fazem reféns e se trancam na Casa da Moeda da Espanha com o ambicioso plano de realizar o maior roubo da história.", 5, "4.9 estrelas", "Úrsula Corberó, Álvaro Morte")
tema_policial.adicionar_serie(serie_casa_de_papel)

tema_drama = Tema("Drama")

serie_breaking_bad = Serie("Breaking Bad", "breakingbad.jpg", "Um professor de química do ensino médio com câncer terminal se junta a um ex-aluno para produzir e vender metanfetamina para garantir o futuro financeiro de sua família.", 6, "4.9 estrelas", "Bryan Cranston, Aaron Paul")
tema_drama.adicionar_serie(serie_breaking_bad)

serie_ozark = Serie("Ozark", "ozark.jpg", "Um consultor financeiro se muda com sua família para as montanhas Ozark para lavar 500 milhões de dólares e acalmar um traficante de drogas.", 4, "4.7 estrelas", "Jason Bateman, Laura Linney")
tema_suspense.adicionar_serie(serie_ozark)

serie_the_witcher = Serie("The Witcher", "witcher.jpg", "Um caçador de monstros solitário luta para encontrar seu lugar em um mundo onde as pessoas frequentemente se provam mais perversas do que as bestas.", 2, "4.6 estrelas", "Henry Cavill, Anya Chalotra")
tema_suspense.adicionar_serie(serie_the_witcher)

serie_the_crown = Serie("The Crown", "thecrown.jpg", "Esta série dramática segue a vida da rainha Elizabeth II desde sua juventude até a atualidade, explorando os eventos históricos que moldaram o segundo reinado mais longo da história britânica.", 5, "4.8 estrelas", "Olivia Colman, Tobias Menzies")
tema_drama.adicionar_serie(serie_the_crown)

serie_gambito = Serie("O Gambito da Rainha", "gambito.jpg", "Em um orfanato dos anos 1950, uma jovem prodígio do xadrez luta contra o vício enquanto enfrenta os melhores jogadores do mundo.", 1, "4.5 estrelas", "Anya Taylor-Joy, Bill Camp")
tema_drama.adicionar_serie(serie_gambito)

serie_suits = Serie("Suits", "suits.jpg", "Mike Ross, um jovem inteligente que abandonou a faculdade de direito, é contratado pelo advogado mais bem-sucedido de Nova York, Harvey Specter, apesar de não ter diploma de direito.", 9, "4.7 estrelas", "Gabriel Macht, Patrick J. Adams")
tema_drama.adicionar_serie(serie_suits)

catalogo = [tema_suspense, tema_policial, tema_drama]