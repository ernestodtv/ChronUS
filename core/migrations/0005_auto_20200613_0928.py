# Generated by Django 2.2.10 on 2020-06-13 07:28

import core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_collaboration_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaboration',
            name='requested_time',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.25), core.validators.validate_minutes]),
        ),
        migrations.AlterField(
            model_name='collaborationrequest',
            name='requested_time',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.25), core.validators.validate_minutes]),
        ),
        migrations.AlterField(
            model_name='degree',
            name='name',
            field=models.CharField(choices=[('0', 'Grado en Administración y Dirección de Empresas'), ('1', 'Grado en Antropología Social y Cultural'), ('2', 'Grado en Ciencias de la Actividad Física y del Deporte'), ('3', 'Grado en Comunicación Audiovisual'), ('4', 'Grado en Criminología'), ('5', 'Grado en Derecho'), ('6', 'Doble Grado en Administración y Dirección de Empresas y en Derecho'), ('7', 'Doble Grado en Derecho y en Economía'), ('8', 'Doble Grado en Derecho y en Finanzas y Contabilidad'), ('9', 'Doble Grado en Derecho y Gestión y Administración Pública'), ('10', 'Doble Grado en Finanzas y Contabilidad y en Relaciones Laborales y Recursos Humanos'), ('11', 'Doble Grado en Geografía y Gestión del Territorio e Historia'), ('12', 'Doble Grado en Periodismo y Comunicación Audiovisual'), ('13', 'Doble Grado en Periodismo y Comunicación Audiovisual (2016)'), ('14', 'Grado en Economía'), ('15', 'Grado en Educación Infantil'), ('16', 'Grado en Educación Primaria'), ('17', 'Grado en Finanzas y Contabilidad'), ('18', 'Grado en Geografía y Gestión del Territorio'), ('19', 'Grado en Gestión y Administración Pública'), ('20', 'Grado en Marketing e Investigación de Mercados'), ('21', 'Grado en Pedagogía'), ('22', 'Grado en Periodismo'), ('23', 'Grado en Publicidad y Relaciones Públicas'), ('24', 'Grado en Relaciones Laborales y Recursos Humanos'), ('25', 'Grado en Turismo'), ('26', 'Grado en Ciencias de la Actividad Física y del Deporte '), ('27', 'Doble Grado en Finanzas y Contabilidad y Relaciones Laborales y Recursos Humanos'), ('28', 'Grado en Arqueología por la Universidad de Granada, Universidad de Jaén y Universidad de Sevilla'), ('29', 'Grado en Bellas Artes'), ('30', 'Grado en Conservación y Restauración de Bienes Culturales'), ('31', 'Doble Grado en Educación Primaria y Estudios Franceses'), ('32', 'Doble Grado en Filología Clásica y Filología Hispánica'), ('33', 'Doble Grado en Lengua y Literatura Alemanas y en Educación Primaria'), ('34', 'Grado en Estudios Árabes e Islámicos'), ('35', 'Grado en Estudios de Asia Oriental por la Universidad de Sevilla y la Universidad de Málaga'), ('36', 'Grado en Estudios Franceses'), ('37', 'Grado en Estudios Ingleses'), ('38', 'Grado en Filología Clásica'), ('39', 'Grado en Filología Hispánica'), ('40', 'Grado en Filosofía'), ('41', 'Grado en Historia'), ('42', 'Grado en Historia del Arte'), ('43', 'Grado en Lengua y Literatura Alemanas'), ('44', 'Grado en Biología'), ('45', 'Grado en Bioquímica por la Universidad de Sevilla y la Universidad de Málaga'), ('46', 'Doble Grado en Física y en Ingeniería de Materiales'), ('47', 'Doble Grado en Física y Matemáticas'), ('48', 'Doble Grado en Matemáticas y Estadística'), ('49', 'Doble Grado en Química y en Ingeniería de Materiales'), ('50', 'Grado en Estadística'), ('51', 'Grado en Física'), ('52', 'Grado en Matemáticas'), ('53', 'Grado en Química'), ('54', 'Grado en Biomedicina Básica y Experimental'), ('55', 'Doble Grado en Farmacia y en Óptica y Optometría'), ('56', 'Doble Grado en Farmacia y en Óptica y Optometría (2019)'), ('57', 'Doble Grado en Fisioterapia y Ciencias de la Actividad Física y del Deporte'), ('58', 'Grado en Enfermería'), ('59', 'Grado en Farmacia'), ('60', 'Grado en Farmacia (2019)'), ('61', 'Grado en Fisioterapia'), ('62', 'Grado en Medicina'), ('63', 'Grado en Odontología'), ('64', 'Grado en Óptica y Optometría'), ('65', 'Grado en Podología'), ('66', 'Grado en Psicología'), ('67', 'Doble Grado en Ingeniería Agrícola (US) y Grado en Ciencias Ambientales (UPO)'), ('68', 'Doble Grado en Ingeniería Eléctrica e Ingeniería Electrónica Industrial'), ('69', 'Doble Grado en Ingeniería Eléctrica e Ingeniería Mecánica'), ('70', 'Doble Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto e Ingeniería Mecánica'), ('71', 'Doble Grado en Ingeniería Informática-Tecnologías Informáticas y en Matemáticas'), ('72', 'Grado en Edificación'), ('73', 'Grado en Fundamentos de Arquitectura'), ('74', 'Grado en Ingeniería Aeroespacial'), ('75', 'Grado en Ingeniería Agrícola'), ('76', 'Grado en Ingeniería Civil'), ('77', 'Grado en Ingeniería de la Energía por la Universidad de Sevilla y la Universidad de Málaga'), ('78', 'Grado en Ingeniería de la Salud por la Universidad de Málaga y la Universidad de Sevilla'), ('79', 'Grado en Ingeniería de las Tecnologías de Telecomunicación'), ('80', 'Grado en Ingeniería de Materiales'), ('81', 'Grado en Ingeniería de Organización Industrial por la Universidad de Málaga y la Universidad de Sevilla'), ('82', 'Grado en Ingeniería de Tecnologías Industriales'), ('83', 'Grado en Ingeniería Eléctrica'), ('84', 'Grado en Ingeniería Electrónica Industrial'), ('85', 'Grado en Ingeniería Electrónica, Robótica y Mecatrónica por la Universidad de Málaga y la Universidad de Sevilla'), ('86', 'Grado en Ingeniería en Diseño Industrial y Desarrollo del Producto'), ('87', 'Grado en Ingeniería Informática-Ingeniería de Computadores'), ('88', 'Grado en Ingeniería Informática-Ingeniería del Software'), ('89', 'Grado en Ingeniería Informática-Tecnologías Informáticas'), ('90', 'Grado en Ingeniería Mecánica'), ('91', 'Grado en Ingeniería Química'), ('92', 'Grado en Ingeniería Química Industrial'), ('93', 'Máster Universitario en Ciencias del Trabajo'), ('94', 'Máster Universitario en Derecho Penal y Ciencias Criminales'), ('95', 'Doble Máster Universitario en Abogacía y Asesoría Jurídico-Mercantil, Fiscal y Laboral'), ('96', 'Doble Máster Universitario en Abogacía y Derecho Público'), ('97', 'Doble Máster Universitario en Abogacía y Relaciones Jurídico-Privadas'), ('98', 'Máster Universitario en Guión, Narrativa y Creatividad Audiovisual (2019)'), ('99', 'Máster Universitario en Abogacía'), ('100', 'Máster Universitario en Actividad Física y Calidad de Vida de Personas Adultas y Mayores'), ('101', 'Máster Universitario en Antropología: Gestión de la Diversidad Cultural, el Patrimonio y el Desarrollo'), ('102', 'Máster Universitario en Asesoría Jurídico-Mercantil, Fiscal y Laboral'), ('103', 'Máster Universitario en Auditoría y Contabilidad Superior'), ('104', 'Máster Universitario en Comunicación Institucional y Política'), ('105', 'Máster Universitario en Comunicación y Cultura'), ('106', 'Máster Universitario en Consultoría Económica y Análisis Aplicado (2018)'), ('107', 'Máster Universitario en Consultoría Laboral'), ('108', 'Máster Universitario en Derecho Constitucional'), ('109', 'Máster Universitario en Derecho Público'), ('110', 'Máster Universitario en Dirección y Planificación del Turismo'), ('111', 'Máster Universitario en Dirección, Evaluación y Calidad de las Instituciones de Formación'), ('112', 'Máster Universitario en Economía y Desarrollo'), ('113', 'Máster Universitario en Estudios Avanzados en Dirección de Empresas (2017)'), ('114', 'Máster Universitario en Estudios de Género y Desarrollo Profesional'), ('115', 'Máster Universitario en Estudios Europeos'), ('116', 'Máster Universitario en Formación y Orientación para el Trabajo'), ('117', 'Máster Universitario en Gestión del Territorio. Instrumentos y Técnicas de Intervención'), ('118', 'Máster Universitario en Gestión Estratégica y Negocios Internacionales'), ('119', 'Máster Universitario en Gestión y Desarrollo de Recursos Humanos'), ('120', 'Máster Universitario en Intervención y Mediación Familiar (2019)'), ('121', 'Máster Universitario en Necesidades Educativas Especiales y Atención a la Diversidad en la Escuela'), ('122', 'Master Universitario en Profesorado de Enseñanza Secundaria Obligatoria y Bachillerato, Formación Profesional y Enseñanza de Idiomas'), ('123', 'Máster Universitario en Psicología de la Educación. Avances en Intervención Psicoeducativa y Necesidades Educativas Especiales'), ('124', 'Máster Universitario en Psicopedagogía'), ('125', 'Máster Universitario en Relaciones Jurídico-Privadas'), ('126', 'Máster Universitario en Profesorado de ESO, Bachiller, FP y Enseñanzas de Idiomas'), ('127', 'Doble M.U. en Est. Hispánicos Superiores y Prof.de ESO y Bachillerato, FP y'), ('128', 'Doble M.U. en Filosofía y Cultura Moderna y Prof.de ESO y Bachillerato, FP'), ('129', 'Doble Máster Universitario en Profesorado de Educación Secundaria Obligatoria y Bachillerato, Formación Profesional y Enseñanza de Idiomas y en Estudios Lingüísticos, Literarios y Culturales'), ('130', 'Máster Universitario en Arqueología por la U.de Sevilla y U.de Granada'), ('131', 'Máster Universitario en Arte: Idea y Producción'), ('132', 'Máster Universitario en Artes del Espectáculo Vivo'), ('133', 'Máster Universitario en Documentos y Libros. Archivos y Bibliotecas'), ('134', 'Máster Universitario en Enseñanza del Español como Lengua Extranjera y de Otras Lenguas Modernas'), ('135', 'Máster Universitario en Escritura Creativa'), ('136', 'Máster Universitario en Estudios Americanos'), ('137', 'Máster Universitario en Estudios Hispánicos Superiores'), ('138', 'Máster Universitario en Estudios Históricos Avanzados'), ('139', 'Máster Universitario en Estudios Lingüísticos, Literarios y Culturales'), ('140', 'Máster Universitario en Filosofía y Cultura Moderna'), ('141', 'Máster Universitario en Patrimonio Artístico Andaluz y su Proyección Iberoamericana'), ('142', 'Máster Universitario en Traducción e Interculturalidad (2017)'), ('143', 'Doble Máster Universitario en Profesorado de Educación Secundaria Obligatoria y Bachillerato, Formación Profesional y Enseñanza de Idiomas (MAES) y en Matemáticas (MUM))'), ('144', 'Máster Erasmus Mundus en Física Nuclear (USE-UAM-UCM-UB-USAL-UCBN-SDP-SCAT)'), ('145', 'Máster Universitario en Biología Avanzada: Investigación y Aplicación'), ('146', 'Máster Universitario en Ciencia y Tecnología de Nuevos Materiales'), ('147', 'Máster Universitario en Estudios Avanzados en Química'), ('148', 'Máster Universitario en Física Nuclear por la Universidad Autónoma de Madrid, la Universidad Complutense de Madrid, la Universidad de Barcelona, la Universidad de Granada, la Universidad de Salamanca y la Universidad de Sevilla'), ('149', 'Máster Universitario en Matemáticas'), ('150', 'Máster Universitario en Microelectrónica: Diseño y Aplicaciones de Sistemas Micro/Nanométricos'), ('151', 'Máster Universitario en Ingeniería Ambiental (2018)'), ('152', 'Máster Universitario en Ingeniería Biomédica y Salud Digital'), ('153', 'Máster Universitario en Ingeniería de Caminos, Canales y Puertos (2019)'), ('154', 'Máster Universitario en Arquitectura'), ('155', 'Máster Universitario en Arquitectura y Patrimonio Histórico'), ('156', 'Máster Universitario en Ciudad y Arquitectura Sostenibles'), ('157', 'Máster Universitario en Diseño Avanzado en Ingeniería Mecánica'), ('158', 'Máster Universitario en Diseño e Ingeniería de Productos e Instalaciones Industriales en Entornos PLM y BIM'), ('159', 'Máster Universitario en Gestión Integral de la Edificación'), ('160', 'Máster Universitario en Ingeniería Aeronáutica'), ('161', 'Máster Universitario en Ingeniería Agronómica'), ('162', 'Máster Universitario en Ingeniería de Caminos, Canales y Puertos'), ('163', 'Máster Universitario en Ingeniería de Telecomunicación'), ('164', 'Máster Universitario en Ingeniería del Software: Cloud, Datos y Gestión de las Tecnologías de la Información'), ('165', 'Máster Universitario en Ingeniería Electrónica, Robótica y Automática'), ('166', 'Máster Universitario en Ingeniería Industrial'), ('167', 'Máster Universitario en Ingeniería Informática'), ('168', 'Máster Universitario en Ingeniería Química'), ('169', 'Máster Universitario en Innovación en Arquitectura: Tecnología y Diseño (2016)'), ('170', 'Máster Universitario en Lógica, Computación e Inteligencia Artificial'), ('171', 'Máster Universitario en Organización Industrial y Gestión de Empresas'), ('172', 'Máster Universitario en Peritación y Reparación de Edificios'), ('173', 'Máster Universitario en Seguridad Integral en Edificación'), ('174', 'Máster Universitario en Seguridad Integral en la Industria y Prevención de Riesgos Laborales'), ('175', 'Máster Universitario en Sistemas de Energía Eléctrica'), ('176', 'Máster Universitario en Sistemas de Energía Térmica'), ('177', 'Máster Universitario en Sistemas Inteligentes en Energía y Transporte por la Universidad de Sevilla y la Universidad de Málaga'), ('178', 'Máster Universitario en Tecnología e Industria Alimentaria'), ('179', 'Máster Universitario en Urbanismo, Planeamiento y Diseño Urbano'), ('180', 'Máster Universitario en Especialización Profesional en Farmacia'), ('181', 'Máster Universitario en Estudios Avanzados en Cerebro y Conducta'), ('182', 'Máster Universitario en Fisiología y Neurociencia'), ('183', 'Máster Universitario en Genética Molecular y Biotecnología'), ('184', 'Máster Universitario en Investigación Biomédica'), ('185', 'Máster Universitario en Investigación Médica: Clínica y Experimental'), ('186', 'Máster Universitario en Migraciones Internacionales, Salud y Bienestar: Modelos y Estrategias de Intervención'), ('187', 'Máster Universitario en Nuevas Tendencias Asistenciales en Ciencias de la Salud'), ('188', 'Máster Universitario en Odontología Médico-Quirúrgica e Integral'), ('189', 'Máster Universitario en Odontología Restauradora, Estética y Funcional'), ('190', 'Máster Universitario en Psicología de la Intervención Social y Comunitaria'), ('191', 'Máster Universitario en Psicología de las Organizaciones y del Trabajo'), ('192', 'Máster Universitario en Psicología General Sanitaria'), ('193', 'Máster Universitario en Odontología Infantil')], max_length=3),
        ),
    ]
