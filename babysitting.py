from flask import Flask, render_template_string

app = Flask(__name__)

# CONFIGURAÇÃO: Cola o teu link do Google Form aqui
LINK_GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSeq75u7mY86Wq4WY6HJaGfL9VVkjXiqrQIlbHc59_zkNFD11Q/viewform?usp=dialog"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-H0ZYDH9HHG"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-H0ZYDH9HHG');
</script>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Passo em Frente | Apoio Escolar & Confiança</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

        :root {
            --orange: #ff6b35;
            --navy: #003049;
            --soft-blue: #f1f4f9;
            --text: #2d3436;
        }

        body { font-family: 'Outfit', sans-serif; margin: 0; color: var(--text); line-height: 1.6; scroll-behavior: smooth; }

        header { 
            display: flex; justify-content: space-between; align-items: center; 
            padding: 20px 8%; background: white; position: sticky; top: 0; z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }
        .logo { font-weight: 700; font-size: 1.5rem; color: var(--navy); }
        .nav-btn { background: var(--orange); color: white; padding: 12px 25px; border-radius: 8px; text-decoration: none; font-weight: 600; transition: 0.3s; border: none; cursor: pointer; }
        .nav-btn:hover { background: var(--navy); transform: translateY(-2px); }

        .hero { 
            display: flex; align-items: center; padding: 80px 8%; 
            background: linear-gradient(rgba(255,255,255,0.8), rgba(255,255,255,0.8)), url('https://images.unsplash.com/photo-1516627145497-ae6968895b74?q=80&w=2040&auto=format&fit=crop');
            background-size: cover; min-height: 450px;
        }
        .hero h1 { font-size: 3rem; color: var(--navy); line-height: 1.1; margin-bottom: 20px; }
        
        .hero-content p { font-size: 1.1rem; margin-bottom: 10px; }

        .age-badge {
            display: inline-block; background: var(--navy); color: white; padding: 5px 15px; border-radius: 50px; font-weight: 600; font-size: 0.9rem; margin-bottom: 15px;
        }

        .section { padding: 80px 8%; text-align: center; }

        .pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin-top: 40px; }
        .price-card { background: white; padding: 40px; border-radius: 20px; border: 1px solid #eee; transition: 0.3s; position: relative; }
        .price-card.featured { border: 2px solid var(--orange); transform: scale(1.05); z-index: 1; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .price-card h3 { color: var(--navy); margin-bottom: 10px; }
        .price-card .price { font-size: 2.5rem; font-weight: 800; color: var(--orange); margin-bottom: 20px; }
        .price-card .price span { font-size: 1rem; color: #666; font-weight: 400; }
        .price-list { list-style: none; padding: 0; margin-bottom: 30px; text-align: left; }
        .price-list li { margin-bottom: 12px; font-size: 0.95rem; }
        .price-list li i { color: #2ecc71; margin-right: 10px; }

        .payment-info {
            background: white; 
            padding: 30px; 
            border-radius: 15px; 
            border: 2px solid var(--soft-blue); 
            margin-top: 40px; 
            max-width: 600px; 
            margin-left: auto; 
            margin-right: auto;
            text-align: center;
        }
        
        .payment-title {
            color: var(--navy); 
            font-size: 1.3rem; 
            font-weight: 700; 
            margin-bottom: 15px;
        }
        .payment-text {
            font-size: 1rem; 
            color: #555; 
            line-height: 1.6;
        }

        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; margin-top: 40px; }
        .service-card { background: white; padding: 30px; border-radius: 15px; border: 2px solid var(--soft-blue); text-align: left; }
        .service-card i { font-size: 2rem; color: var(--orange); margin-bottom: 15px; display: block; text-align: center; }
        .service-card h3 { text-align: center; margin-bottom: 15px; }
        
        .service-card small { 
            display: block; 
            font-size: 0.85rem; 
            color: var(--orange); 
            margin-top: 15px; 
            font-style: italic; 
            line-height: 1.4;
        }

        .steps-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px; margin-top: 50px; }
        .step-card { padding: 40px; background: var(--soft-blue); border-radius: 20px; }
        .step-icon { font-size: 2.5rem; color: var(--orange); margin-bottom: 20px; }

        .features { background: var(--navy); color: white; padding: 80px 8%; }
        .feature-item { display: flex; gap: 20px; margin-bottom: 30px; align-items: flex-start; }
        .feature-item i { color: var(--orange); font-size: 1.5rem; }

        .testimonials { background: #fdfdfd; padding: 80px 8%; text-align: center; }
        .test-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-top: 40px; }
        .test-card { background: white; padding: 30px; border-radius: 15px; border: 1px solid #eee; text-align: left; }
        .stars { color: #f1c40f; margin-bottom: 10px; }

        .form-section { background: var(--soft-blue); padding: 80px 8%; text-align: center; }
        .form-card { background: white; padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); max-width: 500px; margin: 0 auto; }

        footer { background: var(--navy); color: #cbd5e1; padding: 80px 8% 40px; }
        .footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 50px; }
        .footer-col h4 { color: white; margin-bottom: 25px; }
        .footer-bottom { margin-top: 60px; padding-top: 30px; border-top: 1px solid #1e3a8a; text-align: center; }

        .portugal-flag {
            width: 20px; display: inline-block; vertical-align: middle; margin-left: 8px; border-radius: 2px;
        }

        @media (max-width: 768px) { 
            .hero h1 { font-size: 2.5rem; } 
            .price-card.featured { transform: scale(1); } 
            .payment-info { margin: 40px 20px 0; padding: 25px 20px; }
        }
        
        .footer-col a { color: #cbd5e1; text-decoration: none; transition: 0.3s; }
        .footer-col a:hover { color: var(--orange); }
    </style>
</head>
<body>

<header>
    <div class="logo">Passo em Frente</div>
    <a href="#reservar" class="nav-btn">RESERVAR AGORA</a>
</header>

<section class="hero">
    <div class="hero-content">
        <div class="age-badge"><i class="fas fa-info-circle"></i> Serviços para crianças a partir de 1 ano</div>
        <p style="color: var(--orange); font-weight: 700; text-transform: uppercase;">Paço de Arcos & Arredores</p>
        <h1>Educação e cuidado para o seu filho.</h1>
        <p>Guilherme, 20 anos. Dedicado ao apoio escolar e à organização de rotinas.</p>
    </div>
</section>

<section class="section" id="precos">
    <h2 style="font-size: 2.5rem; color: var(--navy);">Preçário</h2>
    <p>Valores transparentes adaptados às suas necessidades.</p>
    
    <div class="pricing-grid">
        <div class="price-card">
            <h3>Essencial</h3>
            <div class="price">5€ <span>/ hora</span></div>
            <ul class="price-list">
                <li><i class="fas fa-check"></i> Babysitting Básico</li>
                <li><i class="fas fa-check"></i> Vigilância em Brincadeiras</li>
                <li><i class="fas fa-check"></i> <b>Gestão de Sestas / Dormir</b></li>
                <li><i class="fas fa-check"></i> Apoio na Higiene</li>
                <li><i class="fas fa-times" style="color:#ccc"></i> Apoio Escolar Ativo</li>
            </ul>
            <a href="#reservar" class="nav-btn" style="background: var(--navy); display:block;">Selecionar</a>
        </div>

        <div class="price-card featured">
            <div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: var(--orange); color: white; padding: 5px 15px; border-radius: 50px; font-size: 0.8rem; font-weight: 700;">MAIS POPULAR</div>
            <h3>Educação</h3>
            <div class="price">12€ <span>/ hora</span></div>
            <ul class="price-list">
                <li><i class="fas fa-check"></i> Babysitting Completo</li>
                <li><i class="fas fa-check"></i> <b>Apoio Escolar (TPC)</b></li>
                <li><i class="fas fa-check"></i> Aquecimento de Refeições</li>
                <li><i class="fas fa-check"></i> Gestão de Rotinas (Banho/Sono)</li>
            </ul>
            <a href="#reservar" class="nav-btn" style="display:block;">Selecionar</a>
        </div>

        <div class="price-card">
            <h3>Noite / Fim de Semana</h3>
            <div class="price">12€ <span>/ hora</span></div>
            <ul class="price-list">
                <li><i class="fas fa-check"></i> Período Noturno </li>
                <li><i class="fas fa-check"></i> Sábados e Domingos</li>
                <li><i class="fas fa-check"></i> Apoio em Eventos Especiais</li>
                <li><i class="fas fa-check"></i> Jogos Didáticos S/ Ecrãs</li>
            </ul>
            <a href="#reservar" class="nav-btn" style="background: var(--navy); display:block;">Selecionar</a>
        </div>
    </div>

    <div class="payment-info">
        <div class="payment-title">Pagamentos via MB WAY</div>
        <div class="payment-text">
            Pagamentos efetuados <strong>após a confirmação da reserva</strong>.<br>
            Pode pagar no <strong>dia do serviço</strong> ou no <strong>final do serviço</strong>.
        </div>
    </div>
</section>

<section class="section" style="background-color: var(--soft-blue);">
    <h2 style="font-size: 2.5rem; color: var(--navy);">O que ofereço</h2>
    <div class="services-grid">
        <div class="service-card">
            <i class="fas fa-baby"></i>
            <h3>Babysitting</h3>
            <p>Cuido dos seus filhos com atenção e responsabilidade — preparo o jantar, brinco com eles e garanto que ficam bem até à hora de dormir. <b>(Disponível para crianças > 1 ano)</b></p>
        </div>
        <div class="service-card">
            <i class="fas fa-book-open"></i>
            <h3>Apoio Escolar</h3>
            <p>Ajudo nos trabalhos de casa e no reforço das matérias escolares (1º e 2º Ciclo).</p>
        </div>
        <div class="service-card">
            <i class="fas fa-clock"></i>
            <h3>Rotina Diária</h3>
            <p>Acompanho nas atividades, preparo refeições e coloco para dormir com segurança e tranquilidade. 
            <small>Nota: Garanto o acompanhamento e aquecimento de refeições já preparadas.</small></p>
        </div>
    </div>
</section>

<section class="section">
    <h2 style="font-size: 2.5rem; color: var(--navy);">O meu serviço em 3 passos</h2>
    <div class="steps-grid">
        <div class="step-card">
            <div class="step-icon"><i class="fas fa-envelope-open-text"></i></div>
            <h3>1. Contacto</h3>
            <p>Preencha o formulário abaixo com os detalhes.</p>
        </div>
        <div class="step-card">
            <div class="step-icon"><i class="fas fa-comments"></i></div>
            <h3>2. Entrevista</h3>
            <p>Conversamos para alinhar rotinas e expectativas.</p>
        </div>
        <div class="step-card">
            <div class="step-icon"><i class="fas fa-check-double"></i></div>
            <h3>3. Confiança</h3>
            <p>Cuidado garantido com foco total na criança.</p>
        </div>
    </div>
</section>

<section class="features">
    <div style="max-width: 800px; margin: 0 auto;">
        <h2 style="font-size: 2.5rem; margin-bottom: 40px; text-align: center;">Porquê escolher o Guilherme?</h2>
        <div class="feature-item"><i class="fas fa-graduation-cap"></i><div><h4>Diferencial Académico</h4><p>Apoio estruturado aos trabalhos de casa.</p></div></div>
        <div class="feature-item"><i class="fas fa-shield-alt"></i><div><h4>Gestão de Rotinas Segura</h4><p>Prioridade máxima no bem-estar e segurança.</p></div></div>
        <div class="feature-item"><i class="fas fa-gamepad"></i><div><h4>Brincadeira Ativa</h4><p>Parceiro ideal para atividades longe dos ecrãs.</p></div></div>
    </div>
</section>

<section class="testimonials">
    <h2 style="font-size: 2.5rem; color: var(--navy);">O que as famílias dizem</h2>
    <div class="test-grid">
        <div class="test-card">
            <div class="stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
            <p>"O Guilherme ajudou imenso o meu filho com os TPC. Recomendo!"</p>
            <p><strong>— Maria Silva (Paço de Arcos)</strong></p>
        </div>
        <div class="test-card">
            <div class="stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
            <p>"Finalmente um babysitter que brinca mesmo com as crianças."</p>
            <p><strong>— João Pereira (Oeiras)</strong></p>
        </div>
    </div>
</section>

<section id="reservar" class="form-section">
    <h2 style="font-size: 2.5rem; color: var(--navy);">Reservar Agora</h2>
    <div class="form-card">
        <p><b>Nota:</b> Apenas aceito pedidos para crianças com 1 ano ou mais.</p>
        <br>
        <a href="{{ google_form_link }}" target="_blank" class="nav-btn" style="display: block;">ABRIR FORMULÁRIO GOOGLE</a>
    </div>
</section>

<footer>
    <div class="footer-grid">
        <div class="footer-col">
            <div class="logo" style="color: white; margin-bottom: 20px;">Passo em Frente</div>
            <p>Confiança e educação em Paço de Arcos.</p>
        </div>
        <div class="footer-col">
            <h4>Saber Mais</h4>
            <p><a href="/sobre-mim" target="_blank">Sobre Mim</a></p> <p>Serviços<br>Preços</p>
        </div>
        <div class="footer-col">
            <h4>Contacto</h4>
            <p>guilhermebabysitter.pt@gmail.com</p>
            <p>Paço de Arcos, Oeiras e arredores</p>
        </div>
    </div>
    <div class="footer-bottom">
        &copy; 2026 Passo em Frente. Profissionalismo e Dedicação.
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_Portugal.svg/600px-Flag_of_Portugal.svg.png" alt="Portugal" class="portugal-flag">
    </div>
</footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, google_form_link=LINK_GOOGLE_FORM)

@app.route('/sobre-mim')
def sobre_mim():
    SOBRE_TEMPLATE = """
    <!DOCTYPE html>
    <html lang="pt-PT">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sobre Mim | Guilherme Bravo</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
            :root { --orange: #ff6b35; --navy: #003049; --soft-blue: #f1f4f9; --text: #2d3436; }
            body { font-family: 'Outfit', sans-serif; margin: 0; color: var(--text); background: var(--soft-blue); display: flex; align-items: center; justify-content: center; min-height: 100vh; }
            .container { max-width: 700px; background: white; padding: 50px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); text-align: center; }
            h1 { color: var(--navy); font-size: 2.5rem; margin-bottom: 20px; }
            .content p { font-size: 1.1rem; line-height: 1.8; color: #555; text-align: left; }
            .back-btn { display: inline-block; margin-top: 30px; background: var(--orange); color: white; padding: 12px 25px; border-radius: 8px; text-decoration: none; font-weight: 600; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Sobre Mim</h1>
            <div class="content">
                <p>Olá! O meu nome é <strong>Guilherme Bravo</strong>, tenho 20 anos e sou o responsável pelo projeto "Passo em Frente".</p>
                <p>O meu objetivo é oferecer mais do que um simples serviço de babysitting. Procuro ser um apoio real para as famílias, focando-me na educação, no apoio escolar (TPC) e na criação de rotinas saudáveis para as crianças.</p>
                <p>Com foco na zona de Paço de Arcos e Oeiras, baseio o meu trabalho na máxima confiança, segurança e dedicação total ao bem-estar dos mais novos.</p>
            </div>
            <a href="/" class="back-btn">Voltar ao Início</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(SOBRE_TEMPLATE)

if __name__ == '__main__':

    app.run(debug=True)

