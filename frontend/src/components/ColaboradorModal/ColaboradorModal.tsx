import { useEffect, useState } from "react";
import type { Colaborador } from "../../types/colaborador";
import "./ColaboradorModal.css";

interface Props {
    open: boolean;
    onClose: () => void;
    onSave: (data: Omit<Colaborador, "id">) => Promise<void>;
    colaborador?: Colaborador | null;
}

const initialState: Omit<Colaborador, "id"> = {
    nome: "",
    matricula: "",
    email: "",
    telefone: "",
    cargo: "",
    setor: "",
    cidade: "",
    data_admissao: "",
    status: "ATIVO",
    foto_url: "",
    observacoes: "",
    gestor_id: null,
};

export default function ColaboradorModal({
    open,
    onClose,
    onSave,
    colaborador,
}: Props) {

    const [form, setForm] = useState(initialState);

    useEffect(() => {
        if (colaborador) {
            const { id, ...rest } = colaborador;
            setForm(rest);
        } else {
            setForm(initialState);
        }
    }, [colaborador]);

    function handleChange(
        e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>
    ) {
        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });
    }

    async function handleSubmit(e: React.FormEvent) {
        e.preventDefault();

        await onSave(form);

        onClose();
    }

    if (!open) return null;

    return (
        <div className="modal-overlay">

            <div className="modal">

                <h2>
                    {colaborador ? "Editar Colaborador" : "Novo Colaborador"}
                </h2>

                <form onSubmit={handleSubmit}>

                    <input
                        name="nome"
                        placeholder="Nome"
                        value={form.nome}
                        onChange={handleChange}
                        required
                    />

                    <input
                        name="matricula"
                        placeholder="Matrícula"
                        value={form.matricula}
                        onChange={handleChange}
                        required
                    />

                    <input
                        name="email"
                        placeholder="E-mail"
                        value={form.email ?? ""}
                        onChange={handleChange}
                    />

                    <input
                        name="telefone"
                        placeholder="Telefone"
                        value={form.telefone ?? ""}
                        onChange={handleChange}
                    />

                    <input
                        name="cargo"
                        placeholder="Cargo"
                        value={form.cargo}
                        onChange={handleChange}
                        required
                    />

                    <input
                        name="setor"
                        placeholder="Setor"
                        value={form.setor}
                        onChange={handleChange}
                        required
                    />

                    <input
                        name="cidade"
                        placeholder="Cidade"
                        value={form.cidade}
                        onChange={handleChange}
                        required
                    />

                    <input
                        type="date"
                        name="data_admissao"
                        value={form.data_admissao}
                        onChange={handleChange}
                        required
                    />

                    <select
                        name="status"
                        value={form.status}
                        onChange={handleChange}
                    >
                        <option value="ATIVO">Ativo</option>
                        <option value="FERIAS">Férias</option>
                        <option value="AFASTADO">Afastado</option>
                        <option value="DESLIGADO">Desligado</option>
                    </select>

                    <textarea
                        name="observacoes"
                        placeholder="Observações"
                        value={form.observacoes ?? ""}
                        onChange={handleChange}
                    />

                    <div className="modal-buttons">

                        <button
                            type="button"
                            onClick={onClose}
                        >
                            Cancelar
                        </button>

                        <button type="submit">
                            Salvar
                        </button>

                    </div>

                </form>

            </div>

        </div>
    );
}