import { useEffect, useState } from "react";
import "./FeriasModal.css";

import type { Colaborador } from "../../types/colaborador";
import type { FeriasPayload, Ferias } from "../../services/feriasService";

interface Props {
    open: boolean;
    onClose: () => void;
    onSave: (data: FeriasPayload) => Promise<void>;
    ferias?: Ferias | null;
    colaboradores: Colaborador[];
}

const initialState: FeriasPayload = {
    colaborador_id: "",
    data_inicio: "",
    data_fim: "",
    status: "PENDENTE",
    observacoes: "",
};

export default function FeriasModal({
    open,
    onClose,
    onSave,
    ferias,
    colaboradores,
}: Props) {

    const [form, setForm] = useState(initialState);

    useEffect(() => {

        if (ferias) {

            const { id, ...rest } = ferias;

            setForm(rest);

        } else {

            setForm(initialState);

        }

    }, [ferias]);

    function handleChange(
        e: React.ChangeEvent<
            HTMLInputElement |
            HTMLSelectElement |
            HTMLTextAreaElement
        >
    ) {

        setForm({
            ...form,
            [e.target.name]: e.target.value,
        });

    }

    async function handleSubmit(
        e: React.FormEvent
    ) {

        e.preventDefault();

        await onSave(form);

        onClose();

    }

    if (!open) return null;

    return (

        <div className="modal-overlay">

            <div className="modal">

                <h2>

                    {ferias ? "Editar Férias" : "Nova Férias"}

                </h2>

                <form onSubmit={handleSubmit}>

                    <select
                        name="colaborador_id"
                        value={form.colaborador_id}
                        onChange={handleChange}
                        required
                    >

                        <option value="">
                            Selecione um colaborador
                        </option>

                        {colaboradores.map((c) => (

                            <option
                                key={c.id}
                                value={c.id}
                            >
                                {c.nome}
                            </option>

                        ))}

                    </select>

                    <input
                        type="date"
                        name="data_inicio"
                        value={form.data_inicio}
                        onChange={handleChange}
                        required
                    />

                    <input
                        type="date"
                        name="data_fim"
                        value={form.data_fim}
                        onChange={handleChange}
                        required
                    />

                    <select
                        name="status"
                        value={form.status}
                        onChange={handleChange}
                    >

                        <option value="PENDENTE">
                            Pendente
                        </option>

                        <option value="APROVADA">
                            Aprovada
                        </option>

                        <option value="CANCELADA">
                            Cancelada
                        </option>

                        <option value="CONCLUIDA">
                            Concluída
                        </option>

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