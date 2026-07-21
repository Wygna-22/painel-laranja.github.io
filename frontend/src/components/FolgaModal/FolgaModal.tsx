import { useEffect, useState } from "react";
import "./FolgaModal.css";

import type { Colaborador } from "../../types/colaborador";
import type { Folga, FolgaPayload } from "../../types/folga";

interface Props {
    open: boolean;
    onClose: () => void;
    onSave: (data: FolgaPayload) => Promise<void>;
    folga?: Folga | null;
    colaboradores: Colaborador[];
}

const initialState: FolgaPayload = {
    colaborador_id: "",
    data: "",
    status: "PENDENTE",
    motivo: "",
    observacoes: "",
};

export default function FolgaModal({
    open,
    onClose,
    onSave,
    folga,
    colaboradores,
}: Props) {

    const [form, setForm] = useState(initialState);

    useEffect(() => {

        if (folga) {

            const { id, ...rest } = folga;

            setForm(rest);

        } else {

            setForm(initialState);

        }

    }, [folga]);

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

                    {folga ? "Editar Folga" : "Nova Folga"}

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
                        name="data"
                        value={form.data}
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

                    </select>

                    <input
                        name="motivo"
                        placeholder="Motivo"
                        value={form.motivo}
                        onChange={handleChange}
                        required
                    />

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