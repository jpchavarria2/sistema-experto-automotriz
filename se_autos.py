import tkinter as tk
from tkinter import ttk, messagebox
import clips

class AutoExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto Automotriz")
        self.root.state('zoomed')
        self.root.configure(bg="#f0f0f0")

        style = ttk.Style(root)
        style.theme_use('clam')
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", foreground="#333333", font=("Helvetica", 10))
        style.configure("TLabelframe", background="#f0f0f0", foreground="#333", font=("Helvetica", 11, "bold"), bordercolor="#ccc", padding=10)
        style.configure("TLabelframe.Label", background="#f0f0f0", foreground="#333", font=("Helvetica", 11, "bold"))
        style.configure("Large.TCheckbutton", background="#f0f0f0", font=("Helvetica", 11))

        style.configure("Diagnose.TButton", font=("Helvetica", 10, "bold"), padding=10, background="#007bff", foreground="white")
        style.map("Diagnose.TButton", background=[('active', '#0056b3')])
        style.configure("Clear.TButton", font=("Helvetica", 10, "bold"), padding=10, background="#6c757d", foreground="white")
        style.map("Clear.TButton", background=[('active', '#5a6268')])

        self.env = clips.Environment()
        self._setup_clips_rules()

        self.sintomas = {
            "no-start": tk.BooleanVar(), "clicking-sound": tk.BooleanVar(),
            "no-sound": tk.BooleanVar(), "dim-lights": tk.BooleanVar(),
            "overheating": tk.BooleanVar(), "steam-from-hood": tk.BooleanVar(),
            "oil-light-on": tk.BooleanVar(), "engine-knocking": tk.BooleanVar(),
            "squeaking-brakes": tk.BooleanVar(), "steering-wheel-shakes": tk.BooleanVar()
        }
        self._create_widgets()

    def _setup_clips_rules(self):
        """
        Configura el motor de inferencia del sistema experto.
        """
        self.env.build('(deftemplate sintoma (slot type))')
        self.env.build('(deftemplate diagnostico (slot result))')
        rules = [
            """(defrule rule-bateria-agotada (sintoma (type no-start)) (sintoma (type clicking-sound)) => (assert (diagnostico (result "Problema de Batería.\n\nCausa Probable: Batería descargada o terminales sucios/sueltos.\n\nRecomendación: Revise y limpie los terminales. Intente pasar corriente. Si no funciona, es probable que necesite una batería nueva."))))""",
            """(defrule rule-motor-arranque (sintoma (type no-start)) (sintoma (type no-sound)) => (assert (diagnostico (result "Falla en el Motor de Arranque.\n\nCausa Probable: El motor de arranque no recibe energía o está dañado.\n\nRecomendación: Verifique las conexiones eléctricas del motor de arranque. Si las luces del tablero encienden bien pero no hay sonido al girar la llave, es muy probable que el motor de arranque deba ser reemplazado."))))""",
            """(defrule rule-sobrecalentamiento (sintoma (type overheating)) (sintoma (type steam-from-hood)) => (assert (diagnostico (result "Sobrecalentamiento del Motor.\n\nCausa Probable: Nivel bajo de refrigerante, fuga en el sistema de enfriamiento o termostato defectuoso.\n\nRecomendación: ¡Deténgase inmediatamente! No abra el radiador en caliente. Espere a que el motor se enfríe y revise el nivel de refrigerante. Rellene si es necesario y busque fugas."))))""",
            """(defrule rule-pastillas-freno (sintoma (type squeaking-brakes)) => (assert (diagnostico (result "Pastillas de Freno Desgastadas.\n\nCausa Probable: Las pastillas han llegado al final de su vida útil.\n\nRecomendación: Reemplace las pastillas de freno lo antes posible. Ignorar este problema puede dañar los discos de freno, resultando en una reparación más costosa."))))""",
            """(defrule rule-balanceo-llantas (sintoma (type steering-wheel-shakes)) => (assert (diagnostico (result "Problema de Balanceo de Llantas.\n\nCausa Probable: Las llantas están desbalanceadas o mal alineadas.\n\nRecomendación: Lleve su vehículo a un taller para un servicio de balanceo y alineación. Mejorará la seguridad y la vida útil de sus neumáticos."))))""",
            """(defrule rule-alternador-fallando (sintoma (type no-start)) (sintoma (type dim-lights)) => (assert (diagnostico (result "Falla del Alternador.\n\nCausa Probable: El alternador no está recargando la batería correctamente.\n\nRecomendación: Es probable que la batería esté descargada porque el alternador no funciona. Necesitará que un mecánico revise el sistema de carga y posiblemente reemplace el alternador."))))""",
            """(defrule rule-bajo-aceite (sintoma (type oil-light-on)) (sintoma (type engine-knocking)) => (assert (diagnostico (result "¡Nivel de Aceite Críticamente Bajo!\n\nCausa Probable: Falta de aceite en el motor, lo que causa fricción y daños internos.\n\nRecomendación: ¡Detenga el motor INMEDIATAMENTE para evitar daños graves! Revise el nivel de aceite y rellene si es necesario. Si la luz persiste, no mueva el coche y llame a una grúa."))))""",
            """(defrule rule-sin-diagnostico (declare (salience -10)) (not (diagnostico)) => (assert (diagnostico (result "Diagnóstico no Concluyente.\n\nNo se pudo determinar un problema claro con los síntomas proporcionados.\n\nRecomendación: Para un diagnóstico preciso, se aconseja consultar a un mecánico profesional."))))"""
        ]
        for rule in rules:
            self.env.build(rule)

    def _create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        sintomas_container = ttk.Frame(main_frame)
        sintomas_container.pack(fill=tk.X, expand=False)
        sintomas_container.grid_columnconfigure(0, weight=1)
        sintomas_container.grid_columnconfigure(1, weight=1)
        sintomas_container.grid_columnconfigure(2, weight=1)
        
        arranque_frame = self._create_symptom_category(sintomas_container, "Arranque y Eléctricos", 0)
        self._add_symptom(arranque_frame, "El auto no enciende", "no-start")
        self._add_symptom(arranque_frame, "Se escucha un 'clic' al arrancar", "clicking-sound")
        self._add_symptom(arranque_frame, "No se escucha ningún sonido", "no-sound")
        self._add_symptom(arranque_frame, "Luces del tablero tenues", "dim-lights")

        motor_frame = self._create_symptom_category(sintomas_container, "Motor y Rendimiento", 1)
        self._add_symptom(motor_frame, "Aguja de temperatura alta", "overheating")
        self._add_symptom(motor_frame, "Sale vapor del capó", "steam-from-hood")
        self._add_symptom(motor_frame, "Luz de aceite encendida", "oil-light-on")
        self._add_symptom(motor_frame, "Golpeteo en el motor", "engine-knocking")

        conduccion_frame = self._create_symptom_category(sintomas_container, "Conducción y Frenos", 2)
        self._add_symptom(conduccion_frame, "Los frenos rechinan", "squeaking-brakes")
        self._add_symptom(conduccion_frame, "El volante tiembla", "steering-wheel-shakes")

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=25)

        diagnose_button = ttk.Button(button_frame, text="Obtener Diagnóstico", command=self.run_diagnostico, style="Diagnose.TButton", width=25)
        diagnose_button.pack(side=tk.LEFT, expand=True, padx=10)

        clear_button = ttk.Button(button_frame, text="Limpiar", command=self.clear_all, style="Clear.TButton", width=25)
        clear_button.pack(side=tk.RIGHT, expand=True, padx=10)

        result_frame = ttk.LabelFrame(main_frame, text="Resultado del Diagnóstico")
        result_frame.pack(fill=tk.BOTH, expand=True)

        self.result_text = tk.Text(result_frame, wrap=tk.WORD, font=("Helvetica", 12), state='disabled', bg="#ffffff", relief="flat", borderwidth=0, padx=10, pady=10)
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def _create_symptom_category(self, parent, title, col):
        frame = ttk.LabelFrame(parent, text=title)
        frame.grid(row=0, column=col, sticky="nswe", padx=5, pady=5)
        return frame

    def _add_symptom(self, parent, text, key):
        cb = ttk.Checkbutton(parent, text=text, variable=self.sintomas[key], style="Large.TCheckbutton")
        cb.pack(anchor="w", padx=15, pady=8)

    def run_diagnostico(self):
        self.env.reset()
        selected_sintomas_count = 0
        for key, var in self.sintomas.items():
            if var.get():
                self.env.assert_string(f'(sintoma (type {key}))')
                selected_sintomas_count += 1

        if selected_sintomas_count == 0:
            messagebox.showwarning("Sin Síntomas", "Por favor, seleccione al menos un síntoma.")
            return

        self.env.run()
        diagnostico_result = ""
        for fact in self.env.facts():
            if fact.template.name == 'diagnostico':
                diagnostico_result = fact['result']
                break
        self.display_result(diagnostico_result)

    def clear_all(self):
        for var in self.sintomas.values():
            var.set(False)
        self.display_result("")

    def display_result(self, text):
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)
        self.result_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoExpertSystem(root)
    root.mainloop()
