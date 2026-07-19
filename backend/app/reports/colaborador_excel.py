from app.reports.base_excel import BaseExcelReport

class ColaboradorExcel(BaseExcelReport):

    def __init__(self, colaboradores):
        self.colaboradores = colaboradores

    def get_title(self):
        return "Relatório de Colaboradores"

    def get_headers(self):

        return [
            "Nome",
            "Email",
            "Cidade",
            "Gestor",
            "Status",
        ]

    def get_rows(self):

        return [

            [
                c.nome,
                c.email,
                c.cidade,
                c.gestor.nome if c.gestor else "",
                c.status,
            ]

            for c in self.colaboradores
        ]

    def get_footer(self):

        return (
            f"Total de colaboradores: "
            f"{len(self.colaboradores)}"
        )