# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:23:01 2024

@author: jmari
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:35:02 2024

@author: Jorge Castro Porta
"""

import tkinter as tk
from tkinter import ttk, messagebox

class InsiderRiskEvaluator:
    def __init__(self):
        self.psychological_evaluation_score = 0
        self.personal_predisposition_score = 0
        self.stressors_score = 0
        self.worrisome_behavior_score = 0
        self.organizational_failures_score = 0

    def evaluate_psychological(self, neuroticism=False, low_ami_ext=False, ext_psych=False, ext_narc=False, low_responsibility=False, high_psychoticism=False, high_machiavellianism=False, high_narcissism=False):
        self.psychological_evaluation_score = (
            5 * neuroticism +
            5 * low_ami_ext +
            5 * ext_psych +
            5 * ext_narc +
            5 * low_responsibility +
            15 * high_psychoticism +
            15 * high_machiavellianism +
            15 * high_narcissism
        )

    def evaluate_personal_predisposition(self, male=False, social_conflict=False, criminal_record=False):
        self.personal_predisposition_score = (
            5 * male +
            15 * social_conflict +
            15 * criminal_record
        )

    def evaluate_stressors(self, relationship_issues=False, economic_problems=False, professional_dissatisfaction=False, physical_health_problems=False, psychological_health_problems=False, addictions=False):
        self.stressors_score = (
            5 * relationship_issues +
            20 * economic_problems +
            15 * professional_dissatisfaction +
            5 * physical_health_problems +
            10 * psychological_health_problems +
            20 * addictions
        )

    def evaluate_worrisome_behavior(self, performance_drop=False, negative_attitude_superiors=False, negative_attitude_peers=False, work_negligence=False, job_search=False, lifestyle_discrepancy=False, unusual_activity=False):
        self.worrisome_behavior_score = (
            5 * performance_drop +
            5 * negative_attitude_superiors +
            5 * negative_attitude_peers +
            10 * work_negligence +
            10 * job_search +
            15 * lifestyle_discrepancy +
            30 * unusual_activity
        )

    def evaluate_organizational_failures(self, lack_of_attention=False, lack_of_evaluation=False, inappropriate_dismissal=False, disproportionate_reprimand=False, contract_termination=False):
        self.organizational_failures_score = (
            5 * lack_of_attention +
            5 * lack_of_evaluation +
            15 * inappropriate_dismissal +
            10 * disproportionate_reprimand +
            10 * contract_termination
        )

    def calculate_total_score(self):
        total_score = (
            self.psychological_evaluation_score +
            self.personal_predisposition_score +
            self.stressors_score +
            self.worrisome_behavior_score +
            self.organizational_failures_score
        )
        return total_score

    def classify_risk(self):
        total_score = self.calculate_total_score()
        if total_score <= 25:
            return 'Riesgo Bajo', '#27ae60'  # Green
        elif 26 <= total_score <= 50:
            return 'Riesgo Medio', '#e67e22'  # Orange
        elif 51 <= total_score <= 75:
            return 'Riesgo Alto', '#c0392b'  # Red
        else:
            return 'Riesgo Extremo', '#8e44ad'  # Dark Violet

class RiskEvaluatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Insider Risk Evaluator")
        self.root.configure(bg='#ececec')  # Set background color

        self.evaluator = InsiderRiskEvaluator()

        self.create_gui()

    def create_gui(self):
        # Set up the grid layout with headings
        headings = ["Evaluación Psicológica", "Predisposición Personal", "Estresores", "Comportamiento Preocupante", "Fallos Organizacionales"]
        for i, heading in enumerate(headings):
            tk.Label(self.root, text=heading, font=('Roboto', 14, 'bold'), bg='#f5f5f5', fg='#2c3e50').grid(row=0, column=i, padx=10, pady=10)

        # Create dropdowns for each category
        self.create_dropdown("Neuroticismo", "psychological", 1, 0)
        self.create_dropdown("Baja amabilidad-extroversión", "psychological", 3, 0)
        self.create_dropdown("Psicopatía extrema", "psychological", 5, 0)
        self.create_dropdown("Narcisismo extremo", "psychological", 7, 0)
        self.create_dropdown("Baja responsabilidad", "psychological", 9, 0)
        self.create_dropdown("Psicoticismo alto", "psychological", 11, 0)
        self.create_dropdown("Maquiavelismo alto", "psychological", 13, 0)
        self.create_dropdown("Narcisismo alto", "psychological", 15, 0)

        self.create_dropdown("Masculino", "personal", 1, 1)
        self.create_dropdown("Conflicto social", "personal", 3, 1)
        self.create_dropdown("Antecedentes penales", "personal", 5, 1)

        self.create_dropdown("Problemas de relación", "stressors", 1, 2)
        self.create_dropdown("Problemas económicos", "stressors", 3, 2)
        self.create_dropdown("Insatisfacción profesional", "stressors", 5, 2)
        self.create_dropdown("Problemas de salud física", "stressors", 7, 2)
        self.create_dropdown("Problemas de salud psicológica", "stressors", 9, 2)
        self.create_dropdown("Adicciones", "stressors", 11, 2)

        self.create_dropdown("Bajada de rendimiento", "behavior", 1, 3)
        self.create_dropdown("Actitud negativa hacia superiores", "behavior", 3, 3)
        self.create_dropdown("Actitud negativa hacia compañeros", "behavior", 5, 3)
        self.create_dropdown("Negligencia en el trabajo", "behavior", 7, 3)
        self.create_dropdown("Búsqueda de empleo", "behavior", 9, 3)
        self.create_dropdown("Discrepancia en el estilo de vida", "behavior", 11, 3)
        self.create_dropdown("Actividad inusual dentro de los equipos de la empresa", "behavior", 13, 3)

        self.create_dropdown("Falta de atención", "organizational", 1, 4)
        self.create_dropdown("Falta de evaluación", "organizational", 3, 4)
        self.create_dropdown("Despido inapropiado", "organizational", 5, 4)
        self.create_dropdown("Reprimenda desproporcionada", "organizational", 7, 4)
        self.create_dropdown("Terminación de contrato", "organizational", 9, 4)

        # Submit button
        self.submit_button = tk.Button(self.root, text="Evaluar Riesgo", command=self.check_completeness, font=('Roboto', 12, 'bold'), bg='#3498db', fg='#ffffff', relief='flat', padx=10, pady=5)
        self.submit_button.grid(row=17, column=0, columnspan=5, pady=20)

        # Result labels
        self.result_label = tk.Label(self.root, text="Puntuación Total: ", font=('Roboto', 12), bg='#f5f5f5', fg='#2c3e50')
        self.result_label.grid(row=18, column=0, columnspan=5)

        self.risk_label = tk.Label(self.root, text="Nivel de Riesgo: ", font=('Roboto', 14, 'bold'), bg='#f5f5f5')
        self.risk_label.grid(row=19, column=0, columnspan=5)

    def create_dropdown(self, label_text, category, row, column):
        label = tk.Label(self.root, text=label_text, font=('Roboto', 11), bg='#f5f5f5', fg='#2c3e50')
        label.grid(row=row, column=column, sticky="w", padx=5, pady=5)
        var = tk.BooleanVar(value=False)
        dropdown = ttk.Combobox(self.root, textvariable=var, state="readonly", font=('Roboto', 11))
        dropdown['values'] = [False, True]
        dropdown.current(0)
        dropdown.grid(row=row+1, column=column, padx=5, pady=5)
        setattr(self, f"{category}_{label_text.replace(' ', '_').replace('-', '_').lower()}", var)

    def check_completeness(self):
        incomplete_fields = [var.get() is False for var in vars(self).values() if isinstance(var, tk.BooleanVar)]

        if any(incomplete_fields):
            self.show_incomplete_warning()
        else:
            self.evaluate_risk()

    def show_incomplete_warning(self):
        response = messagebox.askquestion("Encuesta Incompleta", "Hay campos sin completar. ¿Deseas calcular el riesgo?", icon='warning')
        if response == 'no':
            return
        else:
            self.evaluate_risk(ignore_incomplete=True)

    def evaluate_risk(self, ignore_incomplete=False):
        # Psychological evaluation
        self.evaluator.evaluate_psychological(
            neuroticism=self.psychological_neuroticismo.get(),
            low_ami_ext=self.psychological_baja_amabilidad_extroversión.get(),
            ext_psych=self.psychological_psicopatía_extrema.get(),
            ext_narc=self.psychological_narcisismo_extremo.get(),
            low_responsibility=self.psychological_baja_responsabilidad.get(),
            high_psychoticism=self.psychological_psicoticismo_alto.get(),
            high_machiavellianism=self.psychological_maquiavelismo_alto.get(),
            high_narcissism=self.psychological_narcisismo_alto.get()
        )

        # Personal predisposition
        self.evaluator.evaluate_personal_predisposition(
            male=self.personal_masculino.get(),
            social_conflict=self.personal_conflicto_social.get(),
            criminal_record=self.personal_antecedentes_penales.get()
        )

        # Stressors
        self.evaluator.evaluate_stressors(
            relationship_issues=self.stressors_problemas_de_relación.get(),
            economic_problems=self.stressors_problemas_económicos.get(),
            professional_dissatisfaction=self.stressors_insatisfacción_profesional.get(),
            physical_health_problems=self.stressors_problemas_de_salud_física.get(),
            psychological_health_problems=self.stressors_problemas_de_salud_psicológica.get(),
            addictions=self.stressors_adicciones.get()
        )

        # Worrisome behavior
        self.evaluator.evaluate_worrisome_behavior(
            performance_drop=self.behavior_bajada_de_rendimiento.get(),
            negative_attitude_superiors=self.behavior_actitud_negativa_hacia_superiores.get(),
            negative_attitude_peers=self.behavior_actitud_negativa_hacia_compañeros.get(),
            work_negligence=self.behavior_negligencia_en_el_trabajo.get(),
            job_search=self.behavior_búsqueda_de_empleo.get(),
            lifestyle_discrepancy=self.behavior_discrepancia_en_el_estilo_de_vida.get(),
            unusual_activity=self.behavior_actividad_inusual_dentro_de_los_equipos_de_la_empresa.get()
        )

        # Organizational failures
        self.evaluator.evaluate_organizational_failures(
            lack_of_attention=self.organizational_falta_de_atención.get(),
            lack_of_evaluation=self.organizational_falta_de_evaluación.get(),
            inappropriate_dismissal=self.organizational_despido_inapropiado.get(),
            disproportionate_reprimand=self.organizational_reprimenda_desproporcionada.get(),
            contract_termination=self.organizational_terminación_de_contrato.get()
        )

        # Calculate total score and classify risk
        total_score = self.evaluator.calculate_total_score()
        risk_level, color = self.evaluator.classify_risk()

        # Update result labels
        self.result_label.config(text=f"Puntuación Total: {total_score}")
        self.risk_label.config(text=f"Nivel de Riesgo: {risk_level}", fg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = RiskEvaluatorApp(root)
    root.mainloop()
