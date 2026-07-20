import {
    BarChart,
    Bar,
    ResponsiveContainer,
    XAxis,
    Tooltip,
} from "recharts";

interface Props {
    data: {
        setor: string;
        quantidade: number;
    }[];
}

export default function CollaboratorsChart({ data }: Props) {
    return (
        <ResponsiveContainer width="100%" height="100%">
            <BarChart data={data}>
                <XAxis dataKey="setor" />
                <Tooltip />

                <Bar
                    dataKey="quantidade"
                    fill="#F97316"
                    radius={[6, 6, 0, 0]}
                />
            </BarChart>
        </ResponsiveContainer>
    );
}