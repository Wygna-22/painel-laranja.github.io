import {
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    Tooltip,
} from "recharts";

interface Props{
    data:{
        cidade:string;
        quantidade:number;
    }[];
}

export default function CityChart({data}:Props){

    return(

        <ResponsiveContainer width="100%" height="100%">

            <BarChart data={data}>

                <XAxis dataKey="cidade"/>

                <Tooltip/>

                <Bar
                    dataKey="quantidade"
                    fill="#F97316"
                    radius={[6,6,0,0]}
                />

            </BarChart>

        </ResponsiveContainer>

    );

}